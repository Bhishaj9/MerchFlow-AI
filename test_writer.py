from agents.writer_agent import WriterAgent
import json

try:
    print("Initializing WriterAgent...")
    agent = WriterAgent()
    print("WriterAgent initialized.")
    
    # Optional: Mock call to verify connectivity?
    # prompt said "Tell me when the Writer Agent is ready". 
    # Just initialization is enough to prove API Key is accepted (usually).
    
    print("Success!")
except Exception as e:
    print(f"Error: {e}")
