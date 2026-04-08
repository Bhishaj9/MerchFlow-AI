import os
import asyncio
import json
import traceback
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from dotenv import load_dotenv

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".heic"}

# Import Agents
from agents.visual_analyst import VisualAnalyst
from agents.memory_agent import MemoryAgent
from agents.writer_agent import WriterAgent

load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent

# Initialize Agents
try:
    visual_agent = VisualAnalyst()
    memory_agent = MemoryAgent()
    writer_agent = WriterAgent()
    
    # Try seeding database, but don't crash if it fails (optional robustness)
    try:
        memory_agent.seed_database()
    except Exception as e:
        print(f"⚠️ Memory Agent Seed Warning: {e}")
        
    print("✅ All Agents Online")
except Exception as e:
    print(f"❌ Agent Startup Failed: {e}")
    # We continue, but endpoints might fail if agents aren't ready.

@app.get("/")
async def read_root():
    landing_page = BASE_DIR / "landingpage.html"
    if not landing_page.exists():
        raise HTTPException(status_code=404, detail="landingpage.html not found")
    return FileResponse(landing_page)


@app.get("/dashboard")
async def read_dashboard():
    dashboard_page = BASE_DIR / "dashboard.html"
    if not dashboard_page.exists():
        raise HTTPException(status_code=404, detail="dashboard.html not found")
    return FileResponse(dashboard_page)

@app.post("/generate-catalog")
async def generate_catalog(file: UploadFile = File(...)):
    file_path = None
    try:
        # 1. Save Temp File securely
        import uuid
        os.makedirs("uploads", exist_ok=True)

        # Use a secure random filename to prevent path traversal
        raw_extension = os.path.splitext(file.filename)[1].lower() if file.filename else ""
        # Strictly whitelist allowed image extensions to prevent injection
        file_extension = raw_extension if raw_extension in ALLOWED_EXTENSIONS else ""

        secure_filename = f"{uuid.uuid4().hex}{file_extension}"
        file_path = f"uploads/{secure_filename}"

        with open(file_path, "wb") as f:
            f.write(await file.read())
        
        # 2. Run AI Pipeline (Sequential)
        print("▶️ Starting Visual Analysis...")
        visual_data = await visual_agent.analyze_image(file_path)
        
        print("▶️ Retrieving Keywords...")
        query = f"{visual_data.get('main_color', '')} {visual_data.get('product_type', 'product')}"
        seo_keywords = await asyncio.to_thread(memory_agent.retrieve_keywords, query)
        
        # 2b. AI Fallback: Generate keywords if Pinecone returns empty
        if not seo_keywords:
            print("🤖 Database empty. Using AI Fallback for SEO keywords.")
            try:
                fallback_prompt = (
                    f"The internal keyword database is empty for this product. "
                    f"Based on these visual features: {json.dumps(visual_data)}, "
                    f"generate a list of 10 high-converting e-commerce SEO tags "
                    f"and return them as a JSON array of strings. Return ONLY the JSON array."
                )
                fallback_response = await asyncio.to_thread(
                    visual_agent.client.models.generate_content,
                    model="gemini-2.5-flash",
                    contents=fallback_prompt
                )
                import re
                match = re.search(r'\[.*\]', fallback_response.text, re.DOTALL)
                if match:
                    seo_keywords = json.loads(match.group(0))
                else:
                    seo_keywords = [tag.strip() for tag in fallback_response.text.split(",") if tag.strip()]
                print(f"✅ AI Fallback generated {len(seo_keywords)} keywords.")
            except Exception as fallback_err:
                print(f"⚠️ AI Fallback also failed: {fallback_err}")
                seo_keywords = []
        
        print("▶️ Writing Listing...")
        listing = await asyncio.to_thread(writer_agent.write_listing, visual_data, seo_keywords)
        
        # 3. Construct Final Payload
        final_data = {
            "visual_data": visual_data,
            "seo_keywords": seo_keywords,
            "listing": listing
        }
        
        return JSONResponse(content=final_data)

    except Exception as e:
        error_details = traceback.format_exc()
        print(f"❌ Error in generate-catalog: {e}")
        print(error_details)
        return JSONResponse(
            content={
                "error": "An internal server error occurred.",
                "type": type(e).__name__
            },
            status_code=500
        )
        
    finally:
        # Cleanup
        if file_path and os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as cleanup_error:
                print(f"⚠️ Cleanup Warning: {cleanup_error}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
