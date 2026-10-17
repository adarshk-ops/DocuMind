import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import rag

app = FastAPI(title="RAG PDF Chatbot")
os.makedirs("uploads", exist_ok=True)
history = [] 

class Question(BaseModel):
    question: str
    source: str | None = None

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(400, "Only PDF files are allowed")
    name = os.path.basename(file.filename)
    path = os.path.join("uploads", name)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    n = rag.build_index(path, name)
    if n == 0:
        raise HTTPException(422, "No text found. Scanned PDFs aren't supported yet.")
    return {"file": name, "chunks": n}

@app.get("/documents")
def documents():
    return {"documents": rag.list_docs()}

@app.post("/ask")
def ask(q: Question):
    answer, sources = rag.ask(q.question, history, q.source)
    history.append(("User", q.question))
    history.append(("Assistant", answer))
    return {"answer": answer, "sources": sources}

@app.get("/history")
def get_history():
    return {"history": history}

@app.delete("/history")
def clear_history():
    history.clear()
    return {"cleared": True}