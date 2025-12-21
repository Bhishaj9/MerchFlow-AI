---
title: MerchFlow AI
emoji: 👟
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# MerchFlow AI

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

MerchFlow AI is a high-performance, multi-agent orchestration system designed to automate the generation of premium e-commerce product listings. By synergizing Computer Vision, Retrieval Augmented Generation (RAG), and Large Language Models (LLMs), it transforms raw product images into SEO-optimized market-ready content.

## 🏗️ Architecture Flow

The system employs a sophisticated event-driven architecture orchestrated by **FastAPI**:

1.  **👁️ Visual Agent (Gemini 1.5)**
    *   **Function**: Zero-shot image analysis.
    *   **Process**: Extracts high-fidelity visual attributes including dominant color palettes, stylistic classifications, and granular item types.
    *   **Engine**: Google Gemini 1.5 Flash (Vision).

2.  **🧠 Memory Agent (Pinecone)**
    *   **Function**: Semantic Search & RAG.
    *   **Process**: Vectorizes visual tags to query a high-dimensional index, retrieving historically high-performing SEO keywords and market trends relevant to the product.
    *   **Engine**: Pinecone Vector Database.

3.  **✍️ Writer Agent (Llama 3)**
    *   **Function**: Creative Synthesis.
    *   **Process**: Fuses visual data with retrieved market intelligence to generate persuasive, conversion-focused title, description, and feature bullets.
    *   **Engine**: Meta Llama 3 (via Groq Cloud).

4.  **⚙️ Orchestrator (FastAPI)**
    *   **Function**: Async Pipeline Management.
    *   **Process**: Handles non-blocking agent execution, error propagation, and API lifecycle management.

5.  **🔗 Post-Processing (n8n)**
    *   **Function**: Automation Webhook.
    *   **Process**: Triggers downstream workflows (database storage, Shopify API integration) via secure webhooks upon successful generation.

## 🚀 Complete Setup

To run this system locally, ensure you have the following environment variables configured in your `.env` file:

```env
GEMINI_API_KEY=your_gemini_key
GROQ_API_KEY=your_groq_key
PINECONE_API_KEY=your_pinecone_key
N8N_WEBHOOK_URL=your_n8n_webhook_url
```

## ⚡ Quick Start

### 1. Installation
Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### 2. Execution
Launch the FastAPI server:

```bash
python main.py
```

The API will be available at `http://localhost:7860`.
