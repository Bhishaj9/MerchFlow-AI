import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class WriterAgent:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.3-70b-versatile"

    def write_listing(self, visual_data: dict, seo_keywords: list) -> dict:
        system_prompt = (
            "You are an expert e-commerce copywriter. "
            "Write a persuasive product listing based on these visual attributes and SEO keywords. "
            "Return JSON with keys: title, description, bullet_points."
        )

        user_content = f"""
        Visual Attributes: {json.dumps(visual_data, indent=2)}
        
        SEO Keywords: {', '.join(seo_keywords)}
        
        Please generate the listing in JSON format.
        """

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ],
                temperature=0.7,
                response_format={"type": "json_object"}
            )

            response_text = completion.choices[0].message.content
            return json.loads(response_text)

        except Exception as e:
            print(f"Error generating listing: {e}")
            return {"error": str(e)}
