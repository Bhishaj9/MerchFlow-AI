import shutil
import subprocess
import sys

def main():
    # Check Status
    gh_path = shutil.which('gh')
    
    if not gh_path:
        # Install
        print("GitHub CLI not found. Installing via winget...")
        try:
            subprocess.run(['winget', 'install', '--id', 'GitHub.cli', '-e'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error installing GitHub CLI: {e}")
            return
        except FileNotFoundError:
            print("Error: 'winget' command not found. Please ensure App Installer is installed.")
            return
            
    # Post-Install Instructions (Runs if installed or if installation succeeded)
    print("\n" + "="*40)
    try:
        # Attempt to use ANSI codes for bold, may not work in all Windows terminals but works in VS Code / modern Windows Terminal
        print("✅ \033[1mGitHub CLI is ready!\033[0m")
    except:
        print("✅ GitHub CLI is ready!")
    print("="*40)
    print("⚠️  IMPORTANT: You must now restart your terminal to reload your PATH.")
    print("👉 After restarting, run this command to log in: gh auth login")

if __name__ == "__main__":
    main()
