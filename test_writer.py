import sys
import json
import unittest
from unittest.mock import MagicMock, patch

# Mock groq module before importing WriterAgent
mock_groq_module = MagicMock()
sys.modules['groq'] = mock_groq_module

# Also mock dotenv
mock_dotenv_module = MagicMock()
sys.modules['dotenv'] = mock_dotenv_module

import os
# We need to make sure we patch the os.getenv that WriterAgent will use
from agents.writer_agent import WriterAgent

class TestWriterAgent(unittest.TestCase):
    @patch.dict('os.environ', {'GROQ_API_KEY': 'test_api_key'})
    def setUp(self):
        self.agent = WriterAgent()
        # Reset the mock state before each test
        self.agent.client.chat.completions.create.reset_mock()

    @patch.dict('os.environ', {}, clear=True)
    def test_init_missing_api_key(self):
        with self.assertRaises(ValueError) as context:
            WriterAgent()
        self.assertTrue("GROQ_API_KEY not found" in str(context.exception))

    def test_write_listing_success(self):
        visual_data = {"color": "red", "type": "shirt"}
        seo_keywords = ["red shirt", "comfortable"]

        expected_json = {
            "title": "Awesome Red Shirt",
            "description": "A very comfortable red shirt.",
            "bullet_points": ["Red", "Comfortable"]
        }

        # Mock the completions create response
        mock_completion = MagicMock()
        mock_completion.choices[0].message.content = json.dumps(expected_json)
        self.agent.client.chat.completions.create.return_value = mock_completion

        result = self.agent.write_listing(visual_data, seo_keywords)

        self.assertEqual(result, expected_json)
        self.agent.client.chat.completions.create.assert_called_once()

        # Verify the args passed to create
        _, kwargs = self.agent.client.chat.completions.create.call_args
        self.assertEqual(kwargs['model'], "llama-3.3-70b-versatile")
        self.assertEqual(kwargs['response_format'], {"type": "json_object"})

    def test_write_listing_api_error(self):
        visual_data = {"color": "red", "type": "shirt"}
        seo_keywords = ["red shirt"]

        self.agent.client.chat.completions.create.side_effect = Exception("API connection error")

        result = self.agent.write_listing(visual_data, seo_keywords)

        self.assertEqual(result, {"error": "API connection error"})
        self.agent.client.chat.completions.create.side_effect = None # cleanup side effect just in case

if __name__ == '__main__':
    unittest.main()
