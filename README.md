# QUANDOC AI

Enterprise-Grade Document Intelligence Platform powered by RAG, Multi-Agent Orchestration, and Local LLMs.

---

## Overview

QUANDOC AI is an advanced AI-powered document intelligence system designed to understand, retrieve, analyze, compare, and reason over uploaded documents using Retrieval-Augmented Generation (RAG).

The system combines semantic retrieval, hybrid search pipelines, reranking strategies, orchestration workflows, memory-aware conversations, and local LLM inference to create a production-style enterprise AI architecture.

Unlike traditional chatbot demos, QUANDOC AI focuses on:

* grounded AI responses
* hallucination reduction
* retrieval quality
* intelligent orchestration
* enterprise-style reasoning workflows

---

# Core Features

* Advanced RAG Architecture
* Hybrid Retrieval (Semantic + BM25)
* Pinecone Vector Database Integration
* Multi-Agent Workflow Orchestration
* LangGraph AI Flows
* Query Rewriting Pipeline
* Context-Aware Memory System
* Reranking Pipeline
* Hallucination Control
* Local LLM Inference using Ollama
* PDF Document Intelligence
* Conversational Document QA
* Enterprise-Style AI Reasoning

---

# Tech Stack

## Backend

* FastAPI
* Python
* Uvicorn

## AI / LLM Stack

* LangChain
* LangGraph
* Ollama
* Phi3 / Llama3 / Mistral
* Nomic Embeddings

## Retrieval & Vector Search

* Pinecone
* Hybrid Retrieval
* BM25
* Semantic Search
* Reranking Pipelines

## AI Engineering Concepts Implemented

* Retrieval-Augmented Generation (RAG)
* Multi-Agent Systems
* AI Orchestration
* Query Rewriting
* Context Grounding
* Hallucination Reduction
* Memory-Aware Conversations
* Workflow Routing
* Intelligent Context Synthesis

---

# System Architecture

```text
User Query
   ↓
Query Rewriter
   ↓
Hybrid Retriever
(BM25 + Semantic Search)
   ↓
Reranker
   ↓
Context Builder
   ↓
LangGraph Orchestrator
   ↓
AI Agent Workflow
   ↓
LLM Response Generation
   ↓
Grounded Enterprise Response
```

---

# Project Structure

```bash
backend/
│
├── app/
│   ├── api/
│   ├── rag/
│   ├── workflows/
│   ├── agents/
│   ├── services/
│   └── main.py
│
├── uploads/
├── requirements.txt
└── .env
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/quandoc-ai.git

cd quandoc-ai/backend
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
PINECONE_API_KEY=your_api_key
PINECONE_INDEX=quandoc-ai
```

---

# Install Ollama

Download:

```text
https://ollama.com
```

Pull models:

```bash
ollama pull phi3

ollama pull nomic-embed-text
```

---

# Run Backend

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Testing QUANDOC AI

## Upload PDF

Use:

* `/upload`
* Upload research paper or enterprise document

---

## Test RAG Query

Example JSON:

```json
{
  "question": "Explain the hybrid retrieval architecture discussed in the document."
}
```

---

## Advanced Testing Questions

### Retrieval Quality

```json
{
  "question": "Summarize the main architecture discussed across multiple sections."
}
```

### Memory Testing

```json
{
  "question": "Compare this section with the previous concept discussed earlier."
}
```

### Hallucination Testing

```json
{
  "question": "What does the document say about quantum blockchain insurance?"
}
```

Expected:

* system should refuse unsupported answers

---

# AI Engineering Challenges Solved

While building QUANDOC AI, several real-world AI engineering problems were addressed:

* hallucinated responses
* retrieval inconsistency
* vector database integration
* reranking quality
* workflow orchestration failures
* context fragmentation
* dependency conflicts
* memory handling
* retrieval latency optimization

---

# Key Learnings

QUANDOC AI was built as a hands-on AI engineering system to deeply understand:

* production-grade RAG systems
* enterprise AI orchestration
* retrieval pipelines
* LLM reliability
* system-level AI debugging
* multi-agent workflow design

The project reinforced an important lesson:

> Real AI engineering is learned by building systems that break — and solving the problems behind them.

---

# Future Improvements

* Streaming responses
* Citation generation
* Multi-modal document support
* OCR pipelines
* Advanced agent routing
* Redis memory layer
* Kubernetes deployment
* Authentication & RBAC
* Real-time collaboration
* Evaluation & observability dashboards

---

# Author

Uzain Mohid

AI Engineering • RAG Systems • GenAI Workflows • Enterprise AI Architecture

---
