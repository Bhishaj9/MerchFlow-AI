import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HF_TOKEN")
model = "Qwen/Qwen2-VL-7B-Instruct"
# Update URL to router
url = f"https://router.huggingface.co/models/{model}"

headers = {"Authorization": f"Bearer {api_key}"}

print(f"Testing URL: {url}")

# Test 1: Simple text generation payload (inputs string)
data_text = {
    "inputs": "Hello",
    "parameters": {"max_new_tokens": 50}
}
print("\n--- Test 1: Text Generation (inputs string) ---")
response = requests.post(url, headers=headers, json=data_text)
print(f"Status: {response.status_code}")
print("Response:", response.text)

# Test 2: VQA format
data_vqa = {
    "inputs": {
        "image": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true",
        "question": "What is in this image?"
    }
}
print("\n--- Test 2: VQA Format ---")
response = requests.post(url, headers=headers, json=data_vqa)
print(f"Status: {response.status_code}")
print("Response:", response.text)

# Test 3: Chat Completions API (OpenAI style)
url_chat = f"https://router.huggingface.co/models/{model}/v1/chat/completions"
print(f"\nTesting URL: {url_chat}")
data_chat = {
    "model": model, # Sometimes required in body
    "messages": [
         {"role": "user", "content": "Hello"}
    ],
    "max_tokens": 50
}
print("\n--- Test 3: Chat Completion ---")
response = requests.post(url_chat, headers=headers, json=data_chat)
print(f"Status: {response.status_code}")
print("Response:", response.text)
