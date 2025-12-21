import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HF_TOKEN")
client = InferenceClient(api_key=api_key)
model = "HuggingFaceM4/idefics2-8b"

print(f"Testing model: {model}")

image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true"

# Format for Idefics2:
# User: ![](<image_url>) <text><end_of_utterance>\nAssistant:
prompt = f"User: ![]({image_url}) Describe this image.<end_of_utterance>\nAssistant:"

print(f"\n--- Testing with text_generation and specific prompt ---")
print(f"Prompt: {prompt}")

try:
    # Use text_generation for models that don't support chat
    response = client.text_generation(
        prompt=prompt,
        model=model,
        max_new_tokens=100
    )
    print("Response:", response)
except Exception as e:
    print("Failed:", e)
