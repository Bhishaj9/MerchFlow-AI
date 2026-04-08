import pytest
import os
import json
import sys
from unittest.mock import MagicMock, patch

# Mock modules that are missing in the environment
mock_groq = MagicMock()
sys.modules["groq"] = mock_groq
sys.modules["dotenv"] = MagicMock()

from agents.writer_agent import WriterAgent

@patch('agents.writer_agent.Groq')
@patch('agents.writer_agent.os.getenv')
def test_write_listing_success(mock_getenv, mock_groq_class):
    # Setup environment mock
    mock_getenv.return_value = "fake_groq_api_key"

    # Setup Groq client mock
    mock_client = MagicMock()
    mock_groq_class.return_value = mock_client

    # Initialize agent
    agent = WriterAgent()

    # Mock the response from Groq
    expected_response = {
        "title": "Amazing Red Shirt",
        "description": "A high-quality red shirt for all occasions.",
        "bullet_points": ["100% Cotton", "Breathable fabric", "Vibrant color"]
    }

    mock_completion = MagicMock()
    mock_completion.choices = [
        MagicMock(message=MagicMock(content=json.dumps(expected_response)))
    ]
    mock_client.chat.completions.create.return_value = mock_completion

    # Input data
    visual_data = {"color": "red", "type": "shirt"}
    seo_keywords = ["cotton", "breathable"]

    # Execute
    result = agent.write_listing(visual_data, seo_keywords)

    # Verify
    assert result == expected_response
    assert "error" not in result
    mock_client.chat.completions.create.assert_called_once()

@patch('agents.writer_agent.Groq')
@patch('agents.writer_agent.os.getenv')
def test_write_listing_error_path(mock_getenv, mock_groq_class):
    # Setup environment mock
    mock_getenv.return_value = "fake_groq_api_key"

    # Setup Groq client mock
    mock_client = MagicMock()
    mock_groq_class.return_value = mock_client

    # Initialize agent
    agent = WriterAgent()

    # Mock an exception in the Groq client
    error_message = "API connection failed"
    mock_client.chat.completions.create.side_effect = Exception(error_message)

    # Input data
    visual_data = {"color": "red"}
    seo_keywords = ["test"]

    # Execute
    result = agent.write_listing(visual_data, seo_keywords)

    # Verify
    assert "error" in result
    assert error_message in result["error"]
    mock_client.chat.completions.create.assert_called_once()

@patch('agents.writer_agent.os.getenv')
def test_writer_agent_init_no_key(mock_getenv):
    # Setup environment mock to return None for GROQ_API_KEY
    mock_getenv.return_value = None

    with pytest.raises(ValueError, match="GROQ_API_KEY not found in environment variables"):
        WriterAgent()
