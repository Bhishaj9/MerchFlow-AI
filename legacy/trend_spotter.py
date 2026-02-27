import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class TrendSpotter:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-flash-latest')
            self.has_key = True
        else:
            self.model = None
            self.has_key = False

    def get_trends(self, niche: str):
        if not self.has_key:
            print("⚠️ No API Key found, using mock data")
            return ['Retro Cat Mom', 'Pixel Art Kitty', 'Cattitude']

        try:
            prompt = f"Generate 5 short, witty, and viral t-shirt text concepts for the niche: {niche}. Return strictly a JSON list of strings."
            response = self.model.generate_content(prompt)
            
            content = response.text
            # Clean up markdown formatting if present
            if "```json" in content:
                content = content.replace("```json", "").replace("```", "")
            elif "```" in content:
                 content = content.replace("```", "")
            
            try:
                trends = json.loads(content)
                if isinstance(trends, list):
                    return trends
                else:
                    return [content]
            except json.JSONDecodeError:
                return [content]

        except Exception as e:
            print(f"❌ Error calling Gemini: {e}")
            return ['Retro Cat Mom', 'Pixel Art Kitty', 'Cattitude']
