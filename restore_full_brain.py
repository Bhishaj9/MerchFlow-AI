import os
import subprocess

def restore_main():
    content = """import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import load_dotenv

# Import Agents
from agents.visual_analyst import VisualAnalyst
from agents.memory_agent import MemoryAgent
from agents.writer_agent import WriterAgent

load_dotenv()
app = FastAPI()

# Initialize All Agents
try:
    visual_agent = VisualAnalyst()
    memory_agent = MemoryAgent()
    writer_agent = WriterAgent()
    
    # Seed memory on startup
    memory_agent.seed_database()
    print("✅ All Agents Online")
except Exception as e:
    print(f"⚠️ Warning: Some agents failed to load: {e}")

# 1. SERVE DASHBOARD AT ROOT
@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open("dashboard.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: dashboard.html not found"

# 2. THE MAIN ORCHESTRATOR ENDPOINT
@app.post("/generate-catalog")
async def generate_catalog(file: UploadFile = File(...)):
    try:
        # A. Save Temp File
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # B. Visual Analysis (The Eyes)
        visual_data = await visual_agent.analyze_image(file_path)
        
        # C. Memory Search (The Context)
        # Create a search query from visual data
        query = f"{visual_data.get('main_color', '')} {visual_data.get('product_type', 'product')}"
        seo_keywords = memory_agent.retrieve_keywords(query)
        
        # D. Write Copy (The Brain)
        listing = writer_agent.write_listing(visual_data, seo_keywords)
        
        # Cleanup
        if os.path.exists(file_path):
            os.remove(file_path)
            
        # Return Full Data Structure
        return JSONResponse(content={
            "visual_data": visual_data,
            "seo_keywords": seo_keywords,
            "listing": listing
        })
    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
"""
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ main.py restored with full agent logic.")

def update_dashboard():
    try:
        with open("dashboard.html", "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace localhost URL with relative path
        new_content = content.replace("http://localhost:8000/generate-catalog", "/generate-catalog")
        
        with open("dashboard.html", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ dashboard.html updated for cloud deployment.")
    except Exception as e:
        print(f"❌ Error updating dashboard.html: {e}")

def deploy():
    print("🚀 Starting Deployment...")
    commands = [
        ["git", "add", "main.py", "dashboard.html"],
        ["git", "commit", "-m", "Restore full brain logic and fix dashboard URL"],
        ["git", "push", "space", "clean_deploy:main"]
    ]
    
    for cmd in commands:
        try:
            print(f"Running: {' '.join(cmd)}")
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running command: {' '.join(cmd)}")
            print(e.stderr)
            # Don't break on commit error as it might be empty
            if "nothing to commit" in e.stderr:
                continue
            # For other errors we might want to continue or stop, but let's try to proceed
    print("✅ Deployment script finished.")

if __name__ == "__main__":
    print("🔧 Restoring Full Brain...")
    restore_main()
    update_dashboard()
    deploy()
