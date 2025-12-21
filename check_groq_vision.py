import os
from groq import Groq
from dotenv import load_dotenv
import base64

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
model = "llama-3.2-11b-vision-preview"

print(f"Testing Groq Vision model: {model}")

# Test 1: Image URL
print("\n--- Test 1: Image URL ---")
try:
    image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true"
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    print("Response:", completion.choices[0].message.content)
except Exception as e:
    print("Groq Vision failed:", e)
