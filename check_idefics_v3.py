import os
import traceback
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HF_TOKEN")
client = InferenceClient(api_key=api_key)
model = "HuggingFaceM4/idefics2-8b"

print(f"Testing model: {model}")

print("\n--- Test 1: Image to Text (Captioning) ---")
try:
    # This might work if the API treats it as captioning
    res = client.image_to_text(
        "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true",
        model=model
    )
    print("Response:", res)
except Exception:
    traceback.print_exc()

print("\n--- Test 2: Text Generation (Simple) ---")
try:
    res = client.text_generation("describe a car", model=model, max_new_tokens=50)
    print("Response:", res)
except Exception:
    traceback.print_exc()
