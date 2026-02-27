import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HF_TOKEN")
client = InferenceClient(api_key=api_key)

print(f"Testing token with microsoft/resnet-50")

try:
    # Pass the URL directly as the input (InferenceClient handles URLs for image tasks)
    result = client.image_classification(
        model="microsoft/resnet-50",
        image="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true"
    )
    print("Success:", result)
except Exception as e:
    print("Failed:", e)
