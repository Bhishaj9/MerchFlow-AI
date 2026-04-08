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

    @patch('os.path.exists', return_value=True)
    @patch('os.path.getsize', return_value=1000)
    @patch('asyncio.to_thread')
    async def test_analyze_image_exception(self, mock_to_thread, mock_getsize, mock_exists):
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

    @patch('os.path.exists', return_value=True)
    @patch('os.path.getsize', return_value=1000)
    @patch('asyncio.to_thread')
    async def test_analyze_image_genai_exception(self, mock_to_thread, mock_getsize, mock_exists):
        # First call (PIL) succeeds, second call (GenAI) fails
        mock_to_thread.side_effect = [MagicMock(), Exception("Gemini API Error")]

        # Call the method
        result = await self.analyst.analyze_image("test.jpg")

        # Verify the fallback dictionary
        self.assertEqual(result["main_color"], "Unknown")
        self.assertIn("Error: Gemini API Error", result["visual_features"][0])


    @patch('os.path.exists')
    @patch('os.path.getsize')
    async def test_analyze_image_invalid_extension(self, mock_getsize, mock_exists):
        mock_exists.return_value = True
        mock_getsize.return_value = 1000  # Valid size

        result = await self.analyst.analyze_image("test.txt")
        self.assertEqual(result["main_color"], "Unknown")
        self.assertTrue(any("Unsupported or insecure file type" in feature for feature in result["visual_features"]))

    @patch('os.path.exists')
    @patch('os.path.getsize')
    async def test_analyze_image_file_too_large(self, mock_getsize, mock_exists):
        mock_exists.return_value = True
        mock_getsize.return_value = 21 * 1024 * 1024  # 21 MB, exceeds limit

        result = await self.analyst.analyze_image("test.jpg")
        self.assertEqual(result["main_color"], "Unknown")
        self.assertTrue(any("File too large" in feature for feature in result["visual_features"]))

    @patch('os.path.exists')
    async def test_analyze_image_not_found(self, mock_exists):
        mock_exists.return_value = False

        result = await self.analyst.analyze_image("test.jpg")
        self.assertEqual(result["main_color"], "Unknown")
        self.assertTrue(any("Image not found" in feature for feature in result["visual_features"]))

if __name__ == '__main__':

    unittest.main()
