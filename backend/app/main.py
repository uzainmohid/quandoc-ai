from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

import shutil
import os

from app.services.pdf_service import load_and_split_pdf
from app.rag.embedder import store_embeddings
from app.workflows.langgraph_flow import run_workflow


# =====================================================
# FASTAPI APP
# =====================================================

app = FastAPI(
    title="YoursDOC AI",
    version="3.0",
    description="Enterprise Cognitive RAG System"
)

# =====================================================
# CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# DIRECTORIES
# =====================================================

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs("chroma_db", exist_ok=True)

# =====================================================
# ROOT
# =====================================================

@app.get("/")
def home():

    return {
        "message": "Harvey AI Backend Running"
    }

# =====================================================
# MULTI PDF UPLOAD
# =====================================================

@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    try:

        # Save file
        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        # Process PDF
        chunks = load_and_split_pdf(
            file_path
        )

        # Store in vector DB
        store_embeddings(
            chunks,
            file.filename
        )

        return {
            "status": "success",
            "document": file.filename,
            "chunks_created": len(chunks),
            "message": "Document added to Harvey AI knowledge base"
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }
# =====================================================
# CHAT MODEL
# =====================================================

class ChatRequest(BaseModel):

    question: str

# =====================================================
# CHAT ROUTE
# =====================================================

@app.post("/chat")
def chat(request: ChatRequest):

    try:

        response, docs = run_workflow(
            request.question
        )

        citations = []
        seen = set()

        for doc in docs:

            source = doc.metadata.get(
                "source",
                "Unknown"
            )

            page = doc.metadata.get(
                "page",
                "Unknown"
            )

            citation = f"{source} (Page {page})"

            if citation not in seen:

                seen.add(citation)

                citations.append(citation)

        final_response = {
            "answer": response,
            "sources": citations
        }

        return final_response

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }