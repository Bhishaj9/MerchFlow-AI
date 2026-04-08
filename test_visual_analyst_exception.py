import sys
import unittest
import asyncio
from unittest.mock import MagicMock, patch

# Mock modules before importing the target class
mock_genai = MagicMock()
sys.modules['google'] = MagicMock()
sys.modules['google.genai'] = mock_genai
sys.modules['PIL'] = MagicMock()
sys.modules['PIL.Image'] = MagicMock()
sys.modules['dotenv'] = MagicMock()

from agents.visual_analyst import VisualAnalyst

class TestVisualAnalystException(unittest.IsolatedAsyncioTestCase):
    @patch.dict('os.environ', {'GEMINI_API_KEY': 'test_key'})
    def setUp(self):
        self.analyst = VisualAnalyst()

    @patch('asyncio.to_thread')
    async def test_analyze_image_exception(self, mock_to_thread):
        # We need to mock asyncio.to_thread because it's used for both PIL.Image.open
        # and self.client.models.generate_content.

        # Let's make it raise an exception on the first call (PIL.Image.open)
        mock_to_thread.side_effect = Exception("Simulated PIL Error")

        # Call the method
        result = await self.analyst.analyze_image("test.jpg")

        # Verify the fallback dictionary is returned correctly
        self.assertEqual(result["main_color"], "Unknown")
        self.assertEqual(result["product_type"], "Unknown")
        self.assertEqual(result["design_style"], "Unknown")
        self.assertTrue(any("Simulated PIL Error" in feature for feature in result["visual_features"]))

        # Verify it was called
        mock_to_thread.assert_called()

    @patch('asyncio.to_thread')
    async def test_analyze_image_genai_exception(self, mock_to_thread):
        # First call (PIL) succeeds, second call (GenAI) fails
        mock_to_thread.side_effect = [MagicMock(), Exception("Gemini API Error")]

        # Call the method
        result = await self.analyst.analyze_image("test.jpg")

        # Verify the fallback dictionary
        self.assertEqual(result["main_color"], "Unknown")
        self.assertIn("Error: Gemini API Error", result["visual_features"][0])

if __name__ == '__main__':
    unittest.main()
