from agents.memory_agent import MemoryAgent
import unittest
from unittest.mock import patch, MagicMock

class TestMemoryAgent(unittest.TestCase):

    @patch('agents.memory_agent.os.getenv')
    @patch('agents.memory_agent.Pinecone')
    @patch('agents.memory_agent.genai.Client')
    def test_retrieve_keywords_error_handling(self, mock_genai_client, mock_pinecone, mock_getenv):
        # Mock env vars so __init__ doesn't fail
        mock_getenv.side_effect = lambda k: 'fake_key' if k in ['GEMINI_API_KEY', 'PINECONE_API_KEY'] else None

        # Setup mock Pinecone index
        mock_pc_instance = MagicMock()
        mock_pinecone.return_value = mock_pc_instance
        mock_pc_instance.list_indexes.return_value = [MagicMock(name='merchflow-index')]
        mock_index = MagicMock()
        mock_pc_instance.Index.return_value = mock_index

        agent = MemoryAgent()

        # Mock _get_embedding to raise an Exception
        with patch.object(agent, '_get_embedding', side_effect=Exception("Test mock exception")):
            keywords = agent.retrieve_keywords("test query")
            self.assertEqual(keywords, [])

if __name__ == '__main__':
    try:
        print("Initializing MemoryAgent (original test)...")
        # To avoid making actual calls if .env is missing, we could mock here too,
        # but preserving the original code block as it was.
        agent = MemoryAgent()
        print("Seeding database...")
        agent.seed_database()
        print("Success!")
    except Exception as e:
        print(f"Error (original test code): {e}")

    unittest.main()
