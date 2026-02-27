import os
import subprocess

def update_requirements():
    req_file = "requirements.txt"
    if not os.path.exists(req_file):
        with open(req_file, "w") as f:
            f.write("httpx\n")
        print(f"Created {req_file} with httpx.")
        return

    with open(req_file, "r") as f:
        content = f.read()
    
    if "httpx" not in content:
        with open(req_file, "a") as f:
            f.write("\nhttpx\n")
        print("Appended httpx to requirements.txt.")
    else:
        print("httpx already in requirements.txt.")

def update_main():
    main_content = r'''import os
import httpx
import asyncio
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import load_dotenv
# Import Agents
from agents.visual_analyst import VisualAnalyst
from agents.memory_agent import MemoryAgent
from agents.writer_agent import WriterAgent
load_dotenv()
app = FastAPI()
# Initialize Agents
try:
    visual_agent = VisualAnalyst()
    memory_agent = MemoryAgent()
    writer_agent = WriterAgent()
    memory_agent.seed_database()
    print("✅ All Agents Online")
except Exception as e:
    print(f"⚠️ Agent Startup Warning: {e}")
@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open("dashboard.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Error: dashboard.html not found</h1>"
@app.post("/generate-catalog")
async def generate_catalog(file: UploadFile = File(...)):
    try:
        # 1. Save Temp File
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())
        # 2. Run AI Pipeline
        visual_data = await visual_agent.analyze_image(file_path)
        
        query = f"{visual_data.get('main_color', '')} {visual_data.get('product_type', 'product')}"
        seo_keywords = memory_agent.retrieve_keywords(query)
        
        listing = writer_agent.write_listing(visual_data, seo_keywords)
        
        # 3. Construct Final Payload
        final_data = {
            "visual_data": visual_data,
            "seo_keywords": seo_keywords,
            "listing": listing
        }
        # 4. ⚡ N8N AUTOMATION TRIGGER ⚡
        n8n_url = os.getenv("N8N_WEBHOOK_URL")
        if n8n_url:
            print(f"🚀 Sending data to N8N: {n8n_url}")
            # Fire and forget (don't make the user wait for n8n)
            asyncio.create_task(send_to_n8n(n8n_url, final_data))
        
        # Cleanup
        if os.path.exists(file_path):
            os.remove(file_path)
            
        return JSONResponse(content=final_data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
# Async Helper to send data without blocking
async def send_to_n8n(url, data):
    try:
        async with httpx.AsyncClient() as client:
            await client.post(url, json=data, timeout=5.0)
            print("✅ N8N Webhook Sent Successfully")
    except Exception as e:
        print(f"❌ N8N Webhook Failed: {e}")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
'''
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(main_content)
    print("Updated main.py with N8N integration logic.")

def deploy():
    try:
        subprocess.run(["git", "add", "."], check=True)
        # Check if there are changes to commit
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if status.stdout.strip():
            subprocess.run(["git", "commit", "-m", "Add N8N Integration"], check=True)
            print("Git commit successful.")
        else:
            print("No changes to commit.")
        
        print("Pushing to space...")
        subprocess.run(["git", "push", "space", "clean_deploy:main"], check=True)
        print("✅ Successfully deployed to Hugging Face Space.")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Deployment failed: {e}")

if __name__ == "__main__":
    print("Starting N8N Integration Setup...")
    update_requirements()
    update_main()
    deploy()
    print("✅ connect_n8n.py completed.")
