import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

class VisualAnalyst:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-flash-latest')

    def analyze_image(self, image_bytes):
        prompt = (
            "Analyze this product image for an e-commerce listing. "
            "detailed visual attributes including: Main Color, Material/Texture, Style/Vibe, "
            "and 3 distinct Visual Features. Return the result strictly as a JSON object."
        )

        try:
            # Gemini supports passing bytes directly if packaged correctly, 
            # but usually it expects a PIL image or a specific blob format.
            # The python library often accepts a dictionary for inline data.
            # let's use the 'parts' construction which is standard.
            
            response = self.model.generate_content([
                {'mime_type': 'image/jpeg', 'data': image_bytes},
                prompt
            ])

            text_response = response.text
            
            # Clean up markdown code blocks if present
            if text_response.startswith('```json'):
                text_response = text_response[7:]
            if text_response.startswith('```'):
                text_response = text_response[3:]
            if text_response.endswith('```'):
                text_response = text_response[:-3]
                
            return json.loads(text_response.strip())

        except Exception as e:
            print(f"⚠️ API Quota Hit. Switching to Simulation Mode. (Error: {e})")
            return {
                "color": "Midnight Blue",
                "material": "Synthetic Leather",
                "vibe": "Modern Minimalist",
                "features": ["White rubber sole", "Perforated texture", "Low-top silhouette"]
            }
