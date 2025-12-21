import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HF_TOKEN")
model = "HuggingFaceM4/idefics2-8b"
url = f"https://router.huggingface.co/models/{model}"

headers = {"Authorization": f"Bearer {api_key}"}

print(f"Testing URL: {url}")

# Test A: Simple text inputs
print("\n--- Test A: Simple Text ---")
response = requests.post(url, headers=headers, json={"inputs": "Hello"})
print(f"Status: {response.status_code}")
print("Response:", response.text)

# Test B: Formatted inputs (Standard for some VLM APIs)
# Often they accept { "inputs": "User: ...", "parameters": ... }
print("\n--- Test B: Formatted Prompt ---")
image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true"
prompt = f"User: ![]({image_url}) Describe this image.<end_of_utterance>\nAssistant:"
response = requests.post(url, headers=headers, json={"inputs": prompt, "parameters": {"max_new_tokens": 50}})
print(f"Status: {response.status_code}")
print("Response:", response.text)
