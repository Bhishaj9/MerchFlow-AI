from agents.memory_agent import MemoryAgent

def check_search():
    agent = MemoryAgent()
    query = "urban explorer cargo"
    print(f"Searching for '{query}'...")
    
    embedding = agent._get_embedding(query)
    results = agent.index.query(vector=embedding, top_k=5, include_metadata=True)
    
    for match in results.matches:
        print(f"ID: {match.id} | Score: {match.score:.4f} | Text snippet: {match.metadata.get('text', '')[:50]}")

if __name__ == "__main__":
    check_search()
