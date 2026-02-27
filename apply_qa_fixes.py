import os
import re

def patch_main():
    with open("main.py", "r", encoding="utf-8") as f:
        content = f.read()

    old_pattern = r'return JSONResponse\(\s*content=\{\s*"error": str\(e\),\s*"type": type\(e\)\.__name__,\s*"details": error_details\s*\},\s*status_code=500\s*\)'
    new_text = '''return JSONResponse(
            content={
                "error": "An internal server error occurred.",
                "type": type(e).__name__
            },
            status_code=500
        )'''
    content = re.sub(old_pattern, new_text, content[1:] if content.startswith('\ufeff') else content)

    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Patched main.py")


def patch_memory_agent():
    path = "agents/memory_agent.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_func = r'def retrieve_keywords\(.*?: str\):.*?return \[m\.metadata\[\'keywords\'\] for m in results\.matches if m\.metadata and \'keywords\' in m\.metadata\]'
    new_func = '''def retrieve_keywords(self, query_text: str):
        try:
            query_embedding = self._get_embedding(query_text)
            
            results = self.index.query(
                vector=query_embedding,
                top_k=5,
                include_metadata=True
            )
            return [m.metadata['keywords'] for m in results.matches if m.metadata and 'keywords' in m.metadata]
        except Exception as e:
            print(f"❌ Keyword Retrieval Failed: {e}")
            return []'''
            
    content = re.sub(old_func, new_func, content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Patched agents/memory_agent.py")


def patch_visual_analyst():
    path = "agents/visual_analyst.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Add timeout
    content = content.replace(
        "response = self.model.generate_content([user_prompt, img])",
        "response = self.model.generate_content([user_prompt, img], request_options={'timeout': 15.0})"
    )
    
    if "import re" not in content:
        content = content.replace("import json", "import json\nimport re")

    # Rewrite JSON parsing
    old_parsing = r'# Clean up potential markdown code fences.*?return json\.loads\(cleaned_content\.strip\(\)\)'
    new_parsing = '''# Use regex to find the JSON block robustly
            match = re.search(r'\\{.*\\}', response_text, re.DOTALL)
            if match:
                cleaned_content = match.group(0)
            else:
                cleaned_content = response_text
                
            return json.loads(cleaned_content.strip())'''
            
    content = re.sub(old_parsing, new_parsing, content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Patched agents/visual_analyst.py")


def patch_writer_agent():
    path = "agents/writer_agent.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old_completion = r'completion = self\.client\.chat\.completions\.create\(\s*model=self\.model,\s*messages=\[\s*\{"role": "system", "content": system_prompt\},\s*\{"role": "user", "content": user_content\}\s*\],\s*temperature=0\.7,\s*response_format=\{"type": "json_object"\}\s*\)'

    new_completion = '''completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ],
                temperature=0.7,
                response_format={"type": "json_object"},
                timeout=15.0
            )'''
            
    content = re.sub(old_completion, new_completion, content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Patched agents/writer_agent.py")

if __name__ == "__main__":
    patch_main()
    patch_memory_agent()
    patch_visual_analyst()
    patch_writer_agent()
    print("All file patching completed successfully.")
