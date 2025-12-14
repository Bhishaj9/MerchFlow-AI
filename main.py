from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from agents.visual_analyst import VisualAnalyst
from agents.memory_agent import MemoryAgent
from agents.writer_agent import WriterAgent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize Agents
visual_agent = VisualAnalyst()
memory_agent = MemoryAgent()
memory_agent.seed_database()
writer_agent = WriterAgent()

@app.get("/")
def read_root():
    return {"message": "MerchFlow AI API is running!"}

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    # Use global agent
    image_bytes = await file.read()
    analysis = visual_agent.analyze_image(image_bytes)
    return analysis

@app.post("/generate-catalog")
async def generate_catalog(file: UploadFile = File(...)):
    try:
        # Step 1: Visual Analysis (Eyes)
        image_bytes = await file.read()
        visual_data = visual_agent.analyze_image(image_bytes)
        
        if "error" in visual_data:
             return {"error": "Visual Analysis Failed", "details": visual_data}

        # Step 2: Memory Retrieval (Memory)
        # Construct query from visual attributes
        query_parts = []
        target_keys = ["Main Color", "color", "Material/Texture", "material", "Style/Vibe", "vibe"]
        for key in target_keys:
            if key in visual_data:
                query_parts.append(str(visual_data[key]))
        
        search_query = " ".join(query_parts)
        # Fallback: if no specific keys found, use all string values
        if not search_query:
             search_query = " ".join([str(v) for v in visual_data.values() if isinstance(v, str)])
        
        seo_keywords = memory_agent.retrieve_keywords(search_query)

        # Step 3: Copywriting (Brain)
        listing = writer_agent.write_listing(visual_data, seo_keywords)

        return {
            "visual_data": visual_data,
            "seo_keywords": seo_keywords,
            "listing": listing
        }
    except Exception as e:
        return {"error": f"Orchestration Error: {str(e)}"}

