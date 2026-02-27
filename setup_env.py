import os
import sys
import subprocess
import platform

def main():
    print(f"OS Detected: {platform.system()}")
    
    # Define venv directory
    venv_dir = "venv"
    
    # Create venv
    print(f"Creating virtual environment in '{venv_dir}'...")
    try:
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    except subprocess.CalledProcessError as e:
        print(f"Error creating venv: {e}")
        sys.exit(1)
        
    # Determine pip path based on OS
    if platform.system() == "Windows":
        pip_exe = os.path.join(venv_dir, "Scripts", "pip")
    else:
        pip_exe = os.path.join(venv_dir, "bin", "pip")
        
    # Upgrade pip
    print("Upgrading pip...")
    try:
        subprocess.check_call([pip_exe, "install", "--upgrade", "pip"])
    except subprocess.CalledProcessError as e:
        print(f"Error upgrading pip: {e}")
        
    # Install dependencies
    if os.path.exists("requirements.txt"):
        print("Installing dependencies from requirements.txt...")
        try:
            subprocess.check_call([pip_exe, "install", "-r", "requirements.txt"])
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            sys.exit(1)
    else:
        print("requirements.txt not found.")
        
    print("Setup Complete! Run the server now.")

if __name__ == "__main__":
    main()
