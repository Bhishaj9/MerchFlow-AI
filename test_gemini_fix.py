
import os
import json
from agents.visual_analyst import VisualAnalyst

def test_gemini_visual_analyst():
    print("🚀 Starting Visual Analyst Test (Gemini 1.5 Flash)...")
    
    # 1. Initialize
    try:
        agent = VisualAnalyst()
    except Exception as e:
        print(f"❌ Failed to initialize VisualAnalyst: {e}")
        return

    # 2. Define Image Path (Use a known existing image or creating dummy if needed, 
    #    but better to use one if available. previous context showed 'test_image.jpg')
    image_path = "test_image.jpg"
    if not os.path.exists(image_path):
        print(f"⚠️ {image_path} not found. Using 'screen.jpg' if available or skipping.")
        image_path = "screen.jpg"
        if not os.path.exists(image_path):
            print("❌ No test image found.")
            return

    print(f"📸 Analyzing image: {image_path}")

    # 3. Analyze
    try:
        result = agent.analyze_image(image_path)
        print("✅ Raw Result:", result)
        
        # 4. Verify Structure
        required_keys = ["main_color", "product_type", "design_style", "visual_features"]
        missing = [k for k in required_keys if k not in result]
        
        if missing:
            print(f"❌ Missing keys in JSON: {missing}")
        else:
            print("✅ JSON Structure Validated")
            print("🎨 Main Color:", result.get("main_color"))
            print("📦 Product Type:", result.get("product_type"))

    except Exception as e:
        print(f"❌ Analysis failed with exception: {e}")

if __name__ == "__main__":
    test_gemini_visual_analyst()
