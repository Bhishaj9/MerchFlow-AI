import sys
import os
from unittest.mock import MagicMock, patch

# Mock ALL dependencies that might be missing or require API keys
mock_modules = [
    "dotenv",
    "google",
    "google.genai",
    "pinecone",
    "groq",
    "PIL",
    "fastapi",
    "fastapi.middleware.cors",
    "fastapi.responses",
    "fastapi.testclient",
    "pydantic",
    "starlette",
    "starlette.responses",
    "starlette.middleware.cors",
    "starlette.testclient"
]

for mod in mock_modules:
    sys.modules[mod] = MagicMock()

# --- Mocking CORSMiddleware and FastAPI for internal config verification ---
class MockCORSMiddleware:
    def __init__(self, app, *args, **kwargs):
        self.app = app
        self.args = args
        self.kwargs = kwargs

sys.modules["fastapi.middleware.cors"].CORSMiddleware = MockCORSMiddleware

class MockFastAPI:
    def __init__(self):
        self.middlewares = []
    def add_middleware(self, middleware_class, **kwargs):
        self.middlewares.append((middleware_class, kwargs))
    def get(self, path): return lambda x: x
    def post(self, path): return lambda x: x

sys.modules["fastapi"].FastAPI = MockFastAPI

def test_cors_configuration():
    print("Testing CORS configuration...")
    # Import main with our mocks
    if 'main' in sys.modules:
        del sys.modules['main']
    import main

    found = False
    for mw_class, kwargs in main.app.middlewares:
        if mw_class == MockCORSMiddleware:
            found = True
            assert kwargs["allow_origins"] == ["*"]
            assert kwargs["allow_credentials"] is False
            assert kwargs["allow_methods"] == ["*"]
            assert kwargs["allow_headers"] == ["*"]
            print("✅ CORS Middleware configuration verified!")

    if not found:
        print("❌ CORS Middleware NOT found in app.middlewares")
        sys.exit(1)

def test_agent_regressions():
    print("Testing agent regressions...")
    # Set dummy API keys to avoid initialization errors
    os.environ["GEMINI_API_KEY"] = "test"
    os.environ["PINECONE_API_KEY"] = "test"
    os.environ["GROQ_API_KEY"] = "test"

    from agents.memory_agent import MemoryAgent
    from agents.writer_agent import WriterAgent

    try:
        MemoryAgent()
        print("✅ MemoryAgent initialized successfully (mocked)")
        WriterAgent()
        print("✅ WriterAgent initialized successfully (mocked)")
    except Exception as e:
        print(f"❌ Agent initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_cors_configuration()
    test_agent_regressions()
    print("\n✨ All security fix verifications passed!")
