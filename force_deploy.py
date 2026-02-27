"""
force_deploy.py
Force-deploys the current codebase to the Hugging Face Space.
Handles HF binary file restrictions by untracking offending files first.
"""
import subprocess
import sys

def run(cmd, allow_fail=False):
    print(f"\n>>> {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())
    if result.returncode != 0 and not allow_fail:
        print(f"Command failed with exit code {result.returncode}")
        sys.exit(1)
    return result

if __name__ == "__main__":
    print("=" * 60)
    print("  MerchFlow AI — Force Deploy to Hugging Face Space")
    print("=" * 60)

    # 0. Remove binary files from Git tracking (keep local copies)
    binaries = [
        "stitch_merchflow_ai_dashboard.zip",
        "screen.jpg",
        "test_image.jpg",
    ]
    for b in binaries:
        run(f"git rm --cached {b}", allow_fail=True)

    # Ensure .gitignore blocks them from being re-added
    ignore_entries = binaries + ["*.zip", "*.jpg", "*.jpeg", "*.png"]
    try:
        existing = open(".gitignore", "r").read()
    except FileNotFoundError:
        existing = ""
    with open(".gitignore", "a") as f:
        for entry in ignore_entries:
            if entry not in existing:
                f.write(f"\n{entry}")
    print("\nUpdated .gitignore with binary exclusions.")

    # 1. Stage everything
    run("git add .")

    # 2. Commit (allow fail in case nothing changed)
    run('git commit -m "Critical Deployment: Force update of License, Security Fixes, and Branding"', allow_fail=True)

    # 3. Force push HEAD to space remote's main branch
    run("git push --force space HEAD:main")

    # 4. Print the latest commit for verification
    print("\n" + "=" * 60)
    print("  Deployed Commit:")
    print("=" * 60)
    run("git log -1")

    print("\n✅ Force deploy complete.")
