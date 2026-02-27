import time
import requests
import sys

def test_server():
    base_url = "http://127.0.0.1:8000"
    
    print("⏳ Waiting for server to start...")
    # Retry logic to wait for server
    for i in range(10):
        try:
            response = requests.get(f"{base_url}/")
            if response.status_code == 200:
                print("Server detected!")
                break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            print(f"Attempt {i+1}/10: Server not ready yet...")
    else:
        print("❌ Error: Server failed to start within 10 seconds.")
        sys.exit(1)

    # 1. Health Check (Root Endpoint)
    print("\n🔍 Checking Root Endpoint (/) ...")
    try:
        response = requests.get(f"{base_url}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code != 200:
             print("❌ Root endpoint check failed!")
             sys.exit(1)
    except Exception as e:
        print(f"❌ unexpected error on root check: {e}")
        sys.exit(1)

    # 2. Docs Check (/docs)
    print("\n🔍 Checking Docs Endpoint (/docs) ...")
    try:
        response = requests.get(f"{base_url}/docs")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ API Documentation is accessible.")
        else:
             print(f"❌ Docs endpoint check failed! Status: {response.status_code}")
             sys.exit(1)
             
    except Exception as e:
         print(f"❌ unexpected error on docs check: {e}")
         sys.exit(1)

    print("\n✅ Server is Healthy!")

    # 3. Analyze Trends Check (/analyze-trends/{niche})
    print("\n🔍 Checking Trend Spotter (/analyze-trends/cats) ...")
    try:
        response = requests.get(f"{base_url}/analyze-trends/cats")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")

        if response.status_code == 200:
             print("✅ Trend Spotter is working!")
        else:
             print("❌ Trend Spotter check failed!")
             sys.exit(1)
    except Exception as e:
         print(f"❌ unexpected error on trend spotter check: {e}")
         sys.exit(1)

    # 4. Visionary Agent Check (/generate-design)
    print("\n🔍 Checking Visionary Agent (/generate-design) ...")
    try:
        payload = {"slogan": "Gravity Check", "niche": "Science"}
        response = requests.post(f"{base_url}/generate-design", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")

        if response.status_code == 200:
             print("✅ Visionary is working!")
        else:
             print("❌ Visionary check failed!")
             sys.exit(1)
    except Exception as e:
         print(f"❌ unexpected error on visionary check: {e}")
         sys.exit(1)

    # 5. Manager Agent Check (/run-batch)
    print("\n🔍 Checking Manager Agent (/run-batch) ...")
    try:
        import os
        payload = {"niche": "Coffee"}
        response = requests.post(f"{base_url}/run-batch", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")

        if response.status_code == 200:
            filename = response.json().get("filename")
            results_path = os.path.join("results", filename)
            if os.path.exists(results_path):
                 print(f"✅ Manager is working! CSV created at: {results_path}")
            else:
                 print(f"❌ Batch ran but file not found: {results_path}")
                 sys.exit(1)
        else:
             print("❌ Manager check failed!")
             sys.exit(1)
    except Exception as e:
         print(f"❌ unexpected error on manager check: {e}")
         sys.exit(1)

if __name__ == "__main__":
    test_server()
