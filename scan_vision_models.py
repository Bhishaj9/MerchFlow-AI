import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HF_TOKEN")
headers = {"Authorization": f"Bearer {api_key}"}

candidates = [
    "HuggingFaceM4/idefics2-8b",
    "HuggingFaceM4/idefics2-8b-chatty",
    "llava-hf/llava-1.5-7b-hf",
    "llava-hf/llava-v1.6-mistral-7b-hf",
    "microsoft/Phi-3-vision-128k-instruct",
    "NousResearch/Nous-Hermes-2-Vision-Alpha",
    "OpenGVLab/InternVL-Chat-V1-5",
    "Qwen/Qwen2.5-VL-7B-Instruct",
    "google/paligemma-3b-mix-224"
]

print("Scanning for working Serverless Vision Models...\n")

for model in candidates:
    url = f"https://router.huggingface.co/models/{model}"
    print(f"Testing: {model}")
    try:
        # Simple probe payload
        response = requests.post(url, headers=headers, json={"inputs": "Hello"})
        if response.status_code == 200:
             print(f"✅ WORKS! {model} (Status: 200)")
             print(f"Response: {response.text[:100]}...")
        elif response.status_code == 400:
             # 400 might mean it Exists but input format is wrong (which is good!)
             print(f"⚠️  EXISTS but 400 (Bad Request): {model}")
             print(f"Response: {response.text[:100]}...")
        elif response.status_code == 404:
             print(f"❌ 404 Not Found: {model}")
        else:
             print(f"❌ Error {response.status_code}: {model}")
    except Exception as e:
        print(f"❌ Exception: {e}")
    print("-" * 30)
