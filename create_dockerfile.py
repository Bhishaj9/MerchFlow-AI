import subprocess
import sys

def run_command(command):
    print(f"Running: {command}")
    try:
        # shell=True allows us to run the command string exactly as provided
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e}")
        sys.exit(1)

def main():
    # 1. Create Dockerfile
    dockerfile_content = """FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
# Fix permissions for libraries that write to home
RUN mkdir -p /tmp/home
ENV HOME=/tmp/home
# Start the FastAPI server on port 7860 (required by Hugging Face)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
"""
    
    print("Creating Dockerfile...")
    try:
        with open("Dockerfile", "w", newline='\n') as f:
            f.write(dockerfile_content)
        print("Dockerfile created successfully.")
    except Exception as e:
        print(f"Failed to create Dockerfile: {e}")
        sys.exit(1)

    # 2. Push to Space
    print("Executing Git commands...")
    commands = [
        'git add Dockerfile',
        'git commit -m "Add Dockerfile for Hugging Face deployment"',
        'git push -f space clean_deploy:main'
    ]

    for cmd in commands:
        run_command(cmd)

    print("\ncreate_dockerfile.py execution completed.")

if __name__ == "__main__":
    main()
