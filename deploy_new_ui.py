import re
import subprocess
import sys

def main():
    glassui_path = "glassui.html"
    dashboard_path = "dashboard.html"
    
    # Read the New Design
    try:
        with open(glassui_path, 'r', encoding='utf-8') as f:
            glassui_content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find '{glassui_path}'.")
        sys.exit(1)
        
    # The Safety Scan (Crucial)
    required_ids = [
        "dropZone",
        "fileInput",
        "browseBtn",
        "startBtn",
        "deployBtn",
        "jsonOutput",
        "copyBtn",
        "downloadBtn"
    ]
    
    for element_id in required_ids:
        # Check if id="element_id" or id='element_id' exists
        pattern = rf'id\s*=\s*[\'"]{element_id}[\'"]'
        if not re.search(pattern, glassui_content):
            print(f"⚠️ WARNING: Missing ID {element_id}")
            
    # Overwrite
    try:
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            f.write(glassui_content)
        print(f"Successfully copied '{glassui_path}' to '{dashboard_path}'.")
    except Exception as e:
        print(f"Error overwriting '{dashboard_path}': {e}")
        sys.exit(1)
        
    # Deploy
    print("Deploying to Hugging Face...")
    git_commands = [
        ["git", "add", "dashboard.html"],
        ["git", "commit", "-m", "UI Update: Apply responsive Glassmorphism design from Stitch"],
        ["git", "push", "space", "clean_deploy:main"]
    ]
    
    for cmd in git_commands:
        print(f"Running: {' '.join(cmd)}")
        # Use encoding='utf-8' as strictly requested
        result = subprocess.run(cmd, text=True, encoding='utf-8')
        if result.returncode != 0:
            print(f"Command failed: {' '.join(cmd)}")

if __name__ == "__main__":
    main()
