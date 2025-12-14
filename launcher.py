import subprocess
import time
import webbrowser
import os
import urllib.request
import sys

def is_server_ready(url):
    try:
        with urllib.request.urlopen(url) as response:
            return response.getcode() == 200
    except Exception:
        return False

def main():
    print("🚀 Starting Engine...")
    
    # Definition of the server command
    # Using sys.executable to ensure we use the same python interpreter
    server_command = [sys.executable, "-m", "uvicorn", "main:app", "--reload"]
    
    # Start the server as a subprocess
    process = subprocess.Popen(server_command, cwd=os.getcwd())
    
    server_url = "http://localhost:8000"
    
    # Poll for server availability
    try:
        while not is_server_ready(server_url):
            time.sleep(1)
        
        print("✅ Dashboard Launched")
        
        # Open the dashboard in the default web browser
        dashboard_path = os.path.abspath("dashboard.html")
        webbrowser.open(f"file:///{dashboard_path}")
        
        # Keep the script running to maintain the server process
        process.wait()
        
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        process.terminate()
        process.wait()

if __name__ == "__main__":
    main()
