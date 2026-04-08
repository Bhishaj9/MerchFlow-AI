## 2024-05-18 - [FastAPI Agentic Concurrency]
**Learning:** [In FastAPI agentic pipelines, synchronous third-party API calls (like Pinecone searches or LLM completions) block the main event loop, causing requests to be processed sequentially instead of concurrently. Even if an endpoint is `async def`, any synchronous function call within it will block the entire thread.]
**Action:** [Always use `asyncio.to_thread()` to wrap synchronous network calls (like `Pinecone.Index.query` or Groq completions) inside FastAPI `async def` endpoints or use asynchronous API clients if available. Adding `@lru_cache` to repeated memory retrieval queries drastically reduces external network calls and provides significant speedup.]

## 2024-05-22 - [Optimizing Image I/O in Async Pipelines]
**Learning:** Synchronous image opening operations (e.g., `PIL.Image.open`) can block the FastAPI event loop, particularly with large images or slow file systems. This prevents other concurrent requests from being handled efficiently.
**Action:** Wrap synchronous I/O operations like `PIL.Image.open` in `asyncio.to_thread()` when used within an `async` context to ensure they execute in a separate thread and do not block the main loop.
