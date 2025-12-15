from agents.memory_agent import MemoryAgent

def check():
    agent = MemoryAgent()
    print("Checking for sample_summer_tee_001...")
    fetch_response = agent.index.fetch(ids=["sample_summer_tee_001", "item2"])
    print(fetch_response)

if __name__ == "__main__":
    check()
