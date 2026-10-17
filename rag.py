import os
import fitz
import chromadb
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
llm = genai.GenerativeModel(os.getenv("LLM_NAME", "gemini-3.8-flash"))
embedder = SentenceTransformer("all-MiniLM-L6-v2")
col = chromadb.PersistentClient(path="db").get_or_create_collection("pdf")

def extract_pages(path):
    doc = fitz.open(path)
    return [(i + 1, p.get_text()) for i, p in enumerate(doc)]

def chunk_text(pages, size=200, overlap=40):
    chunks = []
    for page_num, text in pages:
        words = text.split()
        start = 0
        while start < len(words):
            piece = " ".join(words[start:start + size])
            if piece.strip():
                chunks.append({"text": piece, "page": page_num})
            start += size - overlap
    return chunks

def build_index(pdf_path, name):
    chunks = chunk_text(extract_pages(pdf_path))
    if not chunks:
        return 0
    texts = [c["text"] for c in chunks]
    col.upsert(
        ids=[f"{name}-{i}" for i in range(len(chunks))],
        documents=texts,
        embeddings=embedder.encode(texts).tolist(),
        metadatas=[{"page": c["page"], "source": name} for c in chunks],
    )
    return len(chunks)

def list_docs():
    data = col.get(include=["metadatas"])
    return sorted({m["source"] for m in data["metadatas"]})

def ask(question, history, source=None, k=4):
    where = {"source": source} if source else None
    res = col.query(
        query_embeddings=embedder.encode([question]).tolist(),
        n_results=k,
        where=where,
    )
    docs, metas = res["documents"][0], res["metadatas"][0]
    if not docs:
        return "No documents uploaded yet.", []

    context = "\n\n".join(
        f"[{m['source']}, Page {m['page']}] {d}" for d, m in zip(docs, metas)
    )
    chat = "\n".join(f"{role}: {text}" for role, text in history[-6:])
    prompt = f"""Answer using ONLY the context below.
If the answer is not in the context, reply exactly:
"I couldn't find this in the document."
Mention sources like (file.pdf, Page 3).

Chat so far:
{chat}

Context:
{context}

Question: {question}"""
    answer = llm.generate_content(prompt).text
    sources = sorted({(m["source"], m["page"]) for m in metas})
    return answer, [{"source": s, "page": p} for s, p in sources]