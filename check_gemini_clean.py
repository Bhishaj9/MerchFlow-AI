import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

candidates = [
    "gemini-2.0-flash",
    "gemini-2.0-flash-exp",
    "models/gemini-2.0-flash"
]

for model_name in candidates:
    print(f"\nTesting model: {model_name}")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello")
        print(f"✅ Success with {model_name}: {response.text}")
        break
    except Exception as e:
        print(f"❌ Failed with {model_name}: {e}")
