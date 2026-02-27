import os
import time
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
import google.generativeai as genai

load_dotenv()

class MemoryAgent:
    def __init__(self):
        # Configure Gemini
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found")
        genai.configure(api_key=self.gemini_api_key)
        
        # Configure Pinecone
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        if not self.pinecone_api_key:
            raise ValueError("PINECONE_API_KEY not found")
            
        self.pc = Pinecone(api_key=self.pinecone_api_key)
        self.index_name = "merchflow-index"
        
        # Check and create index
        existing_indexes = [i.name for i in self.pc.list_indexes()]
        if self.index_name not in existing_indexes:
            print(f"Creating index {self.index_name}...")
            self.pc.create_index(
                name=self.index_name,
                dimension=768, # models/text-embedding-004 dimension
                metric='cosine',
                spec=ServerlessSpec(
                    cloud='aws',
                    region='us-east-1'
                )
            )
            # Wait for index to be ready
            while not self.pc.describe_index(self.index_name).status['ready']:
                time.sleep(1)
            print("Index created.")
        
        self.index = self.pc.Index(self.index_name)

    def _get_embedding(self, text):
        # Using models/text-embedding-004
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=text,
            task_type="retrieval_document"
        )
        return result['embedding']

    def seed_database(self):
        # Check if empty
        stats = self.index.describe_index_stats()
        if stats.total_vector_count > 0:
            print("Database already seeded.")
            return

        print("Seeding database...")
        items = [
            {
                "id": "item1",
                "text": "Running Shoe",
                "keywords": "breathable, shock absorption, marathon training, lightweight"
            },
            {
                "id": "item2",
                "text": "Graphic T-Shirt",
                "keywords": "100% cotton, vintage wash, pre-shrunk, soft feel"
            },
            {
                "id": "item3",
                "text": "Leather Wallet",
                "keywords": "genuine leather, RFID blocking, minimalist, bifold"
            }
        ]

        vectors = []
        for item in items:
            embedding = self._get_embedding(item['text'])
            vectors.append({
                "id": item['id'],
                "values": embedding,
                "metadata": {"keywords": item['keywords'], "text": item['text']}
            })
        
        self.index.upsert(vectors=vectors)
        print(f"Seeded {len(vectors)} items.")

    def retrieve_keywords(self, query_text: str):
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
            return []
