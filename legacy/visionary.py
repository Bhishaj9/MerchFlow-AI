import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class Visionary:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-flash-latest')
            self.has_key = True
        else:
            self.model = None
            self.has_key = False

    def generate_art_prompt(self, slogan: str, niche: str) -> str:
        if not self.has_key:
            return "Mock visualization: A cute retro cat wearing sunglasses, vector art, pastel colors"

        try:
            system_prompt = (
                f'You are an expert T-shirt Designer. Create a high-quality AI art generation prompt '
                f'for the slogan: "{slogan}" in the niche: "{niche}". '
                f'Specify style (e.g., vector, retro, kawaii), colors, and composition. '
                f'Keep it under 40 words.'
            )
            response = self.model.generate_content(system_prompt)
            return response.text.strip()
        except Exception as e:
            print(f"❌ Error calling Gemini: {e}")
            return "Error generating prompt"
