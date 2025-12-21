import os
import sys
from dotenv import load_dotenv

# Load env variables (for HF_TOKEN)
load_dotenv()

# Add project root to path so we can import agents
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.visual_analyst import VisualAnalyst

def test_hf_vision():
    image_path = "test_image.jpg"
    
    if not os.path.exists(image_path):
        print(f"❌ '{image_path}' not found. Please provide a test image.")
        return

    print(f"🔍 Testing Hugging Face Qwen2-VL Vision Analyst with {image_path}...")
    
    try:
        analyst = VisualAnalyst()
        result = analyst.analyze_image(image_path)
        
        print("\n✅ Analysis Result:")
        print(result)
        
        required_keys = ["main_color", "product_type", "design_style", "visual_features"]
        missing_keys = [k for k in required_keys if k not in result]
        
        if missing_keys:
            print(f"\n❌ Missing keys in response: {missing_keys}")
        else:
            print("\n🎉 Output format verified!")

    except Exception as e:
        print(f"\n❌ Test Failed: {e}")

if __name__ == "__main__":
    test_hf_vision()
