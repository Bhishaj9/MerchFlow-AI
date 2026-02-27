import os
import sys

# Force UTF-8 output for Windows terminals
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update .env
env_path = ".env"
key = "GOOGLE_API_KEY"
value = "AIzaSyDgIkagGBciWNZDTn07OlfY9tVPvo6KJ1on"

print(f"Updating {key} in .env...")

lines = []
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

found = False
new_lines = []
for line in lines:
    if line.startswith(f"{key}="):
        new_lines.append(f"{key}={value}\n")
        found = True
    else:
        new_lines.append(line)

if not found:
    if new_lines and not new_lines[-1].endswith('\n'):
        new_lines.append('\n')
    new_lines.append(f"{key}={value}\n")

with open(env_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"✅ Updated {key} in .env")

# 2. Upload to Cloud
print("Syncing secrets to Hugging Face Space...")
try:
    # Build path to ensure we can import upload_secrets
    sys.path.append(os.getcwd())
    from upload_secrets import upload_secrets
    
    upload_secrets()
    print("✅ Google Key saved locally and uploaded to Hugging Face!")
except Exception as e:
    print(f"❌ Failed to sync: {e}")
