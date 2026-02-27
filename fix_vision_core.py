import os
import subprocess

def fix_vision_core():
    # Content for agents/visual_analyst.py
    content = """import os
import json
import asyncio
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

class VisualAnalyst:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("⚠️ GEMINI_API_KEY missing")

        genai.configure(api_key=api_key)
        # Use the modern, faster Flash model
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def analyze_image(self, image_path: str):
        print(f"👁️ Analyzing image: {image_path}")
        
        try:
            # 1. Load image properly with Pillow (Fixes format issues)
            img = Image.open(image_path)
            
            # 2. Define the prompt
            prompt = \"\"\"
            Analyze this product image for an e-commerce listing.
            Return ONLY a raw JSON object (no markdown formatting) with this structure:
            {
                "main_color": "string",
                "product_type": "string",
                "design_style": "string (minimalist, streetwear, vintage, etc)",
                "visual_features": ["list", "of", "visible", "features"],
                "suggested_title": "creative product title",
                "condition_guess": "new/used"
            }
            \"\"\"
            
            # 3. Run in a thread to prevent blocking (Sync to Async wrapper)
            response = await asyncio.to_thread(
                self.model.generate_content,
                [prompt, img]
            )
            
            # 4. Clean and Parse JSON
            text_response = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(text_response)
        except Exception as e:
            print(f"❌ Vision Error: {e}")
            # Return a Safe Fallback (Simulation)
            return {
                "main_color": "Unknown",
                "product_type": "Unidentified Item",
                "design_style": "Standard",
                "visual_features": ["Error analyzing image"],
                "suggested_title": "Manual Review Needed",
                "condition_guess": "New"
            }
"""
    # Write the file
    os.makedirs("agents", exist_ok=True)
    with open("agents/visual_analyst.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ agents/visual_analyst.py updated.")

    # Git operations
    print("🚀 Pushing to HuggingFace...")
    commands = [
        ["git", "add", "agents/visual_analyst.py"],
        ["git", "commit", "-m", "Fix vision core and error handling"],
        ["git", "push", "space", "clean_deploy:main"]
    ]
    
    for cmd in commands:
        try:
            print(f"Running: {' '.join(cmd)}")
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Command failed: {e}")
            # Continue even if commit fails (e.g. prompt already applied)
            
if __name__ == "__main__":
    fix_vision_core()
