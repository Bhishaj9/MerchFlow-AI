import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HF_TOKEN")
client = InferenceClient(api_key=api_key)
model = "Qwen/Qwen2-VL-7B-Instruct"

print(f"Testing model: {model}")

# Test 1: Text only
print("\n--- Test 1: Text Only ---")
try:
    messages = [
        {"role": "user", "content": "Hello, are you working?"} 
    ]
    completion = client.chat.completions.create(
        model=model, 
        messages=messages, 
        max_tokens=100
    )
    print("Response:", completion.choices[0].message.content)
except Exception as e:
    print("Text only failed:", e)

# Test 2: Image (using a public URL to avoid base64 issues first)
print("\n--- Test 2: Image URL ---")
try:
    image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true"
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": image_url}},
                {"type": "text", "text": "What is in this image?"}
            ]
        }
    ]
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=100
    )
    print("Response:", completion.choices[0].message.content)
except Exception as e:
    print("Image URL failed:", e)
