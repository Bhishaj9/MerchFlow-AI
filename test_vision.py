import os
import sys
import requests

IMAGE_FILENAME = "test_image.jpg"
URL = "http://localhost:8000/analyze-image"

def main():
    # 1. File Check
    if not os.path.exists(IMAGE_FILENAME):
        print(f"❌ Please place a real product image named {IMAGE_FILENAME} in this folder first.")
        sys.exit(1)

    print(f"Found {IMAGE_FILENAME}. Uploading to {URL}...")

    # 2. Upload
    try:
        with open(IMAGE_FILENAME, "rb") as f:
            files = {"file": (IMAGE_FILENAME, f, "image/jpeg")}
            response = requests.post(URL, files=files)
        
        # 3. Result
        if response.status_code == 200:
            print("\n✅ Analysis Complete! Gemini says:")
            print(response.json())
        else:
            print("\n❌ Error from server:")
            print(f"Status: {response.status_code}")
            print(response.text)

    except requests.exceptions.ConnectionError:
        print("\n❌ Could not connect to the server.")
        print("Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
