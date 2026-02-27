import os
import subprocess

def run_command(command):
    try:
        # shell=True is often required on Windows for some commands/environments
        print(f"Running: {command}")
        result = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running: {command}")
        print(e.stderr)
        # We don't exit here to allow attempting subsequent commands or user debugging if one fails,
        # though for git flow it usually makes sense to stop. 
        # Given the instruction is a sequence, we should probably stop if add/commit fails.
        exit(1)

def main():
    license_text = """MIT License

Copyright (c) 2025 Bhishaj

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

    file_path = "LICENSE"
    
    print(f"Creating {file_path}...")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(license_text)
    print(f"{file_path} created successfully.")

    print("Running git commands...")
    
    # 1. git add LICENSE
    run_command("git add LICENSE")
    
    # 2. git commit -m 'Add MIT License'
    run_command("git commit -m \"Add MIT License\"")
    
    # 3. git push space clean_deploy:main
    print("Pushing to Hugging Face Space (this might take a few seconds)...")
    run_command("git push space clean_deploy:main")
    
    print("Done! License added and pushed to Hugging Face Space.")

if __name__ == "__main__":
    main()
