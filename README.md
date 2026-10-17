# DocuMind

DocuMind is a simple, smart PDF assistant that lets you upload documents and ask questions about them in plain English. It reads the PDF, breaks it into smaller chunks, searches the most relevant parts, and uses a Gemini-powered language model to answer your questions with source-aware responses.

Think of it as a lightweight document Q&A assistant for notes, study material, reports, and other PDF-based content.

## What this project does

- Upload PDF files from the browser
- Extract text from the document
- Split the content into searchable chunks
- Store the chunks in a local vector database
- Find the most relevant passages for a question
- Answer using a Gemini LLM with citations/sources
- Keep track of multiple documents and document-specific queries

## Tech stack

- Python
- FastAPI
- PyMuPDF for PDF extraction
- SentenceTransformers for embeddings
- ChromaDB for vector search
- Google Gemini API for generation
- HTML/CSS/JS frontend

## Project structure

- `app.py` — FastAPI server and routes
- `rag.py` — PDF processing, embedding, retrieval, and LLM logic
- `static/index.html` — web interface
- `uploads/` — uploaded PDFs
- `db/` — ChromaDB storage

## Prerequisites

Before running the app, make sure you have:

- Python 3.10+
- A working virtual environment
- A Gemini API key

## Setup

1. Open the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt` file yet, install the required packages manually:

```bash
pip install fastapi uvicorn python-multipart pymupdf sentence-transformers chromadb python-dotenv google-generativeai
```

4. Create a `.env` file in the project root and add your Gemini key:

```env
GEMINI_API_KEY=your_api_key_here
LLM_NAME=gemini-3.8-flash
```

## Run the app

From the project root:

```bash
python main.py
```

Then open:

```text
http://127.0.0.1:8000
```

If needed, you can also run the FastAPI app directly:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

## How to use it

1. Open the app in your browser.
2. Upload a PDF file.
3. Wait while the PDF is indexed.
4. Ask a question in the chat box.
5. View the answer and relevant document references.

## Features

- Multi-document PDF handling
- Intelligent chunk retrieval
- LLM-based answer generation
- Query by selected document source
- Document deletion and history management
- Local persistent vector database

## API overview

The app exposes a few backend endpoints:

- `GET /` — web interface
- `GET /status` — app health and document count
- `POST /upload` — upload a PDF
- `GET /documents` — list indexed documents
- `DELETE /documents/{doc_name}` — remove a document
- `POST /ask` — ask a question against the indexed files
- `GET /history` — view chat history
- `DELETE /history` — clear conversation history

## Notes

- The app uses a local ChromaDB database, so indexed documents persist across runs.
- If your API key is missing or invalid, the app falls back to a simple stub response instead of crashing.
- Some PDFs may not be readable if they are scanned images or password-protected.

## License

This project is intended for local learning and personal use. Add a license if you plan to share or publish it.

## Future improvements

- Better UI polish and responsiveness
- Better citation formatting
- PDF page highlighting for answer references
- User authentication
- Support for larger document collections
- Deployment-ready setup for cloud hosting

## Final note

DocuMind is a practical, beginner-friendly RAG project that demonstrates how AI can answer questions from PDF documents using retrieval and generation together. It is a great base for learning, experimentation, and further customization.

This project was restructured with the help of AI to improve clarity, organization, and maintainability.
