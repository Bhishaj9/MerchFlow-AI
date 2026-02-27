import os
import json
import re
from google import genai
from dotenv import load_dotenv

load_dotenv()

class VisualAnalyst:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found")
        
        self.client = genai.Client(api_key=self.api_key, http_options={'timeout': 180.0})
        self.model_name = "gemini-1.5-flash"
        print(f"✅ VisualAnalyst stored Gemini model: {self.model_name}")

    async def analyze_image(self, image_path: str):
        try:
            # Upload the file to Gemini
            # Note: For efficiency in production, files should be managed (uploads/deletes)
            # but for this agentic flow, we'll upload per request or assume local path usage helper if needed.
            # However, the standard `model.generate_content` can take PIL images or file objects directly for some sdk versions,
            # but using the File API is cleaner for 1.5 Flash multi-modal.
            # Let's use the simpler PIL integration if available, or just path if the SDK supports it.
            # actually, standard genai usage for images usually involves PIL or uploading.
            # Let's try the PIL approach first as it's often more direct for local scripts.
            import PIL.Image
            img = PIL.Image.open(image_path)
            
            user_prompt = (
                "Analyze this product image. "
                "Return ONLY valid JSON with keys: main_color, product_type, design_style, visual_features."
            )
            
            # We'll stick to prompt engineering for now to match the "Return ONLY valid JSON" instruction.
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=[user_prompt, img]
            )
            
            response_text = response.text
            
            # Use regex to find the JSON block robustly
            match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if match:
                cleaned_content = match.group(0)
            else:
                cleaned_content = response_text
                
            return json.loads(cleaned_content.strip())

        except Exception as e:
            print(f"❌ Analysis Failed: {e}")
            return {
                "main_color": "Unknown",
                "product_type": "Unknown", 
                "design_style": "Unknown",
                "visual_features": [f"Error: {str(e)}"]
            }
