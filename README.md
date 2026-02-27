---
title: MerchFlow AI
emoji: 👟
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

<div align="center">

# 🚀 MerchFlow AI

### Autonomous E-Commerce Catalog Intelligence

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Gemini_2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Pinecone](https://img.shields.io/badge/Pinecone-000000?style=for-the-badge&logo=pinecone&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

**Proprietary & Confidential — Bhishaj Technologies**

---

*A multi-agent AI pipeline that converts raw product imagery into enterprise-grade, SEO-optimized e-commerce catalogs in seconds.*

</div>

---

## 🎯 Core Value Proposition

MerchFlow AI eliminates the manual bottleneck of product catalog creation. By orchestrating **Computer Vision**, **Retrieval-Augmented Generation (RAG)**, and **Large Language Models** in a seamless autonomous pipeline, it delivers production-ready product listings — from a single image upload — with zero human intervention.

---

## 🏗️ System Architecture

The system employs a high-performance, event-driven architecture orchestrated by **FastAPI**:

### 👁️ Visual Analyst Agent
- **Function**: Zero-shot product image analysis
- **Process**: Extracts granular visual attributes — dominant colors, material composition, design style, branding elements, and product classification
- **Engine**: `Gemini 2.5 Flash` via the unified **Google GenAI SDK** (`google-genai`)

### 🧠 Semantic Memory Agent
- **Function**: RAG-based keyword retrieval with intelligent fallback
- **Process**: Vectorizes visual attributes to query a high-dimensional index, retrieving historically high-converting SEO keywords and market trends. When the database has no match for a niche, the **Intelligence Fallback** system autonomously generates keywords via Gemini — ensuring **0% empty results**
- **Engine**: `Pinecone Vector DB` with `gemini-embedding-001` embeddings (768 dimensions)

### ✍️ Writer Agent
- **Function**: High-conversion copy synthesis
- **Process**: Fuses visual intelligence with retrieved market data to generate persuasive, conversion-optimized titles, descriptions, and feature bullet points
- **Engine**: `Meta Llama 3.3 70B` (via Groq Cloud)

### ⚙️ Pipeline Orchestrator
- **Function**: Async pipeline management & delivery
- **Process**: Handles non-blocking agent execution, error propagation, and API lifecycle management. Results are delivered instantly through the **Premium Glassmorphism UI**
- **Engine**: `FastAPI` with async/await architecture

---

## 🖥️ Production Interface

MerchFlow AI ships with a **Premium Glassmorphism UI** built for instant catalog generation:

- 🎨 Frosted-glass aesthetic with dynamic gradient backgrounds
- 📤 Drag-and-drop image upload with real-time processing feedback
- 📊 Structured JSON output display for visual data, SEO keywords, and generated listings
- 📱 Fully responsive design across desktop, tablet, and mobile

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Runtime** | Python 3.10+ | Core language |
| **Framework** | FastAPI | Async API orchestration |
| **AI SDK** | `google-genai` (Unified) | Vision & embedding inference |
| **Vision Model** | Gemini 2.5 Flash | Product image analysis |
| **Embeddings** | `gemini-embedding-001` | 768-dim vector generation |
| **Vector DB** | Pinecone (Serverless) | Semantic keyword retrieval |
| **LLM** | Llama 3.3 70B (Groq) | Copywriting synthesis |
| **UI** | Glassmorphism / Tailwind CSS | Production dashboard |
| **Deployment** | Docker / Hugging Face Spaces | Containerized hosting |

---

## 📋 System Updates & Technical Milestones

| Date | Milestone |
|------|-----------|
| **Feb 2026** | ✅ Full migration from deprecated `google-generativeai` to unified `google-genai` SDK |
| **Feb 2026** | ✅ Vision model upgraded to `Gemini 2.5 Flash` for industry-leading latency |
| **Feb 2026** | ✅ Pinecone vector alignment to `768 dimensions` with `gemini-embedding-001` for mathematical precision |
| **Feb 2026** | ✅ **Intelligence Fallback** system deployed — guarantees 0% empty SEO keyword results |
| **Feb 2026** | ✅ n8n webhook decoupled — pipeline relies strictly on the Glassmorphism UI for delivery |
| **Feb 2026** | ✅ Production Glassmorphism dashboard launched |

---

## 🚀 Quick Start

### 1. Environment Configuration

Create a `.env` file in the project root with the following keys:

```env
GEMINI_API_KEY=your_google_genai_api_key
GROQ_API_KEY=your_groq_cloud_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

### 2. Installation

```bash
pip install -r requirements.txt
```

### 3. Launch

```bash
python main.py
```

The production dashboard will be available at `http://localhost:7860`.

---

## 📁 Project Structure

```
MerchFlow-AI/
├── main.py                  # FastAPI orchestrator & pipeline logic
├── dashboard.html           # Glassmorphism production UI
├── Dockerfile               # Container deployment config
├── requirements.txt         # Python dependencies
├── agents/
│   ├── visual_analyst.py    # Gemini 2.5 Flash vision agent
│   ├── memory_agent.py      # Pinecone RAG + embedding agent
│   └── writer_agent.py      # Llama 3.3 copywriting agent
└── .env                     # Environment variables (not tracked)
```

---

## ⚖️ Legal Notice

> **PROPRIETARY & CONFIDENTIAL**
>
> This software, including all source code, documentation, algorithms, and associated intellectual property, is the exclusive proprietary property of **Bhishaj Technologies (UDYAM-UP-02-0108589)**.
>
> Unauthorized copying, distribution, modification, reverse engineering, or any form of reproduction of this software — in whole or in part — is strictly prohibited and may result in legal action under applicable intellectual property laws.
>
> **© 2026 Bhishaj Technologies. All Rights Reserved.**

---

<div align="center">

**Built with precision by Bhishaj Technologies** 🇮🇳

</div>
