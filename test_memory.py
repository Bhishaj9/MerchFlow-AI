from agents.memory_agent import MemoryAgent

try:
    print("Initializing MemoryAgent...")
    agent = MemoryAgent()
    print("Seeding database...")
    agent.seed_database()
    print("Success!")
except Exception as e:
    print(f"Error: {e}")
