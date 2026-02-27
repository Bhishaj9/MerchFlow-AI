import sys
import subprocess

def main():
    dockerfile_path = "Dockerfile"
    
    # Read & Replace
    try:
        with open(dockerfile_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Could not find {dockerfile_path}")
        sys.exit(1)
        
    updated = False
    for i, line in enumerate(lines):
        if line.startswith("FROM python:3.9"):
            lines[i] = "FROM python:3.11-slim\n"
            updated = True
            break
            
    if not updated:
        print("Warning: Could not find 'FROM python:3.9' in Dockerfile. The file might already be updated or use a different base image.")
    
    # Save
    try:
        with open(dockerfile_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print("Successfully updated Dockerfile.")
    except Exception as e:
        print(f"Error writing to Dockerfile: {e}")
        sys.exit(1)
        
    # Deploy
    print("Deploying to Hugging Face...")
    commands = [
        ["git", "add", "Dockerfile"],
        ["git", "commit", "-m", "Chore: Upgrade Docker container to Python 3.11-slim"],
        ["git", "push", "space", "clean_deploy:main"]
    ]
    
    for cmd in commands:
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, text=True, capture_output=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Command failed (stderr): {result.stderr}")
            # we don't exit here so we can see all errors if any

if __name__ == "__main__":
    main()
