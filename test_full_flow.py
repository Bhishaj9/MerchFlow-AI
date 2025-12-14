import os
import sys
import requests
import json

IMAGE_FILENAME = "test_image.jpg"
URL = "http://localhost:8000/generate-catalog"

def main():
    if not os.path.exists(IMAGE_FILENAME):
        print(f"❌ {IMAGE_FILENAME} not found.")
        sys.exit(1)

    print(f"Uploading {IMAGE_FILENAME} to {URL}...")

    try:
        with open(IMAGE_FILENAME, "rb") as f:
            files = {"file": (IMAGE_FILENAME, f, "image/jpeg")}
            response = requests.post(URL, files=files)
        
        if response.status_code == 200:
            print("\n✅ Catalog Generated!")
            data = response.json()
            if "error" in data:
                print(f"❌ Error reported by API: {data['error']}")
                if "details" in data:
                    print(f"Details: {data['details']}")
            else:
                print(json.dumps(data, indent=2))
        else:
            print("\n❌ HTTP Error:")
            print(f"Status: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
