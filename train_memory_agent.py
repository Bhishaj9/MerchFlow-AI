import os
import time
from agents.memory_agent import MemoryAgent

def main():
    print("Initializing MemoryAgent...")
    # Initialize MemoryAgent (handles Pinecone and Gemini setup)
    agent = MemoryAgent()

    # 1. Define Training Data
    # 5-10 high-quality 'sample listings'
    samples = [
        {
            "id": "sample_summer_tee_001",
            "text": "The ultimate summer essential. This heavyweight cotton t-shirt features a boxy fit and dropped shoulders for a relaxed, contemporary silhouette. Finished with a garment dye process for a soft, broken-in feel and vintage aesthetic.",
            "metadata": {"category": "Streetwear", "best_for": "Summer", "price_point": "Premium"}
        },
        {
             "id": "sample_hoodie_002",
             "text": "Engineered for comfort and durability. This fleece hoodie minimizes shrinkage and maintains its shape over time. Features double-needle stitching, a generous kangaroo pocket, and rib-knit cuffs. The style is versatile enough for gym sessions or casual weekends.",
             "metadata": {"category": "Casual", "best_for": "Autumn/Winter", "price_point": "Mid-range"}
        },
        {
            "id": "sample_joggers_003",
            "text": "Performance meets style. These tapered joggers are crafted from moisture-wicking tech fabric with four-way stretch. Designed with articulated knees for maximum mobility and zippered ankle cuffs for easy on/off. Perfect for high-intensity training or athleisure wear.",
            "metadata": {"category": "Activewear", "best_for": "All Season", "price_point": "Performance"}
        },
        {
            "id": "sample_oversized_shirt_004",
            "text": "A statement piece for the modern wardrobe. This oversized button-down is cut from crisp poplin with a dramatic high-low hem. The minimalist design is accented by hidden placket buttons and a sharp collar, offering a clean, architectural look.",
             "metadata": {"category": "Avant-Garde", "best_for": "Spring/Summer", "price_point": "Luxury"}
        },
        {
            "id": "sample_cargo_shorts_005",
            "text": "Rugged utility for the urban explorer. These cargo shorts are built from ripstop cotton canvas. Featuring multiple bellowed pockets with snap closures, reinforced belt loops, and a gusseted crotch. Functional, durable, and ready for adventure.",
            "metadata": {"category": "Streetwear", "best_for": "Summer", "price_point": "Standard"}
        }
    ]

    print(f"Preparing to upload {len(samples)} samples to Pinecone...")

    # 2. Batch Upload
    vectors = []
    for item in samples:
        # Generate embedding using the agent's internal method
        # This ensures we use the exact same model and parameters as the agent
        embedding = agent._get_embedding(item['text'])
        
        # Prepare metadata
        # We include the 'text' in metadata so we can retrieve the full description later
        meta = item['metadata'].copy()
        meta['text'] = item['text'] 
        
        vectors.append({
            "id": item['id'],
            "values": embedding,
            "metadata": meta
        })

    # Upsert to Pinecone
    # Using the agent's underlying index object
    agent.index.upsert(vectors=vectors)
    print("Upload complete. vectors upserted successfully.")

    # 3. Verify
    print("\n--- Verifying Data ---")
    query = "summer t-shirt"
    print(f"Running test search for: '{query}'")
    
    # Generate embedding for the query
    query_embedding = agent._get_embedding(query)
    
    # Query the index
    results = agent.index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True
    )
    
    print(f"Found {len(results.matches)} matches:")
    for match in results.matches:
        print(f"\nID: {match.id}")
        print(f"Score: {match.score:.4f}")
        print(f"Category: {match.metadata.get('category', 'N/A')}")
        print(f"Snippet: {match.metadata.get('text', '')[:100]}...")

if __name__ == "__main__":
    main()
