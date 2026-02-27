import os
import subprocess

def main():
    files_to_delete = [
        "stitch_merchflow_ai_dashboard.zip",
        "screen.jpg",
        "test_image.jpg"
    ]
    
    # Delete Local Binaries
    print("Deleting local binaries...")
    for filename in files_to_delete:
        try:
            os.remove(filename)
            print(f"Deleted: {filename}")
        except FileNotFoundError:
            print(f"File not found (already deleted): {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")
            
    # Update .gitignore
    print("Updating .gitignore...")
    gitignore_path = ".gitignore"
    
    # Read existing content to avoid duplicate entries
    existing_ignores = []
    try:
        if os.path.exists(gitignore_path):
            with open(gitignore_path, "r", encoding="utf-8") as f:
                existing_ignores = f.read().splitlines()
    except Exception as e:
        print(f"Warning: Could not read .gitignore: {e}")
        
    ignores_to_add = ["*.zip", "*.jpg"]
    
    try:
        with open(gitignore_path, "a", encoding="utf-8") as f:
            for ignore in ignores_to_add:
                if ignore not in existing_ignores:
                    # add a newline if files doesn't end with one, but simplier to just write
                    f.write(f"\n{ignore}\n")
                    print(f"Added '{ignore}' to .gitignore")
                else:
                    print(f"'{ignore}' already in .gitignore")
    except Exception as e:
        print(f"Error updating .gitignore: {e}")

    # The Orphan Branch Strategy
    print("\nExecuting Git Orphan Branch Strategy...")
    
    commands = [
        "git checkout --orphan hf_clean_deploy_v2",
        "git add .",
        'git commit -m "UI Update: Glassmorphism Design & Binary Cleanup"'
    ]
    
    for cmd in commands:
        print(f"Running: {cmd}")
        subprocess.run(cmd, shell=True, check=False)
        
    push_cmd = "git push --force space hf_clean_deploy_v2:main"
    print(f"\nRunning final push command: {push_cmd}")
    
    result = subprocess.run(push_cmd, shell=True, capture_output=True, text=True)
    
    # Expected Output
    print("\n--- Push Command STDOUT ---")
    print(result.stdout)
    print("--- Push Command STDERR ---")
    print(result.stderr)
    print("---------------------------\n")

    if result.returncode == 0:
        print("✅ Force push successful!")
    else:
        print("❌ Force push failed (see STDERR above).")

if __name__ == "__main__":
    main()
