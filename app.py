import requests
import streamlit as st

API = "http://127.0.0.1:8000"
st.set_page_config(page_title="RAG PDF Chatbot", page_icon="📄")
st.title("📄 Chat with your PDFs")

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Sidebar ----------
with st.sidebar:
    st.header("Documents")
    uploaded = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded and st.button("Index PDF"):
        with st.spinner("Reading and indexing..."):
            r = requests.post(
                f"{API}/upload",
                files={"file": (uploaded.name, uploaded.getvalue(), "application/pdf")},
                timeout=300,
            )
        if r.ok:
            st.success(f"Indexed {r.json()['chunks']} chunks")
        else:
            st.error(r.json().get("detail", "Upload failed"))

    try:
        docs = requests.get(f"{API}/documents", timeout=10).json()["documents"]
    except requests.exceptions.ConnectionError:
        docs = []
        st.error("Backend is not running. Start it with: uvicorn main:app --reload")

    choice = st.selectbox("Search in", ["All documents"] + docs)

    if st.button("Clear chat"):
        try:
            requests.delete(f"{API}/history", timeout=10)
        except requests.exceptions.ConnectionError:
            pass
        st.session_state.messages = []
        st.rerun()

# ---------- Chat history ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            with st.expander("Sources"):
                for s in msg["sources"]:
                    st.write(f"📄 {s['source']}, page {s['page']}")

# ---------- New question ----------
if q := st.chat_input("Ask something about your PDFs"):
    st.session_state.messages.append({"role": "user", "content": q})
    with st.chat_message("user"):
        st.markdown(q)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                r = requests.post(
                    f"{API}/ask",
                    json={
                        "question": q,
                        "source": None if choice == "All documents" else choice,
                    },
                    timeout=120,
                )
                data = r.json()
                answer, sources = data["answer"], data["sources"]
            except Exception as e:
                answer, sources = f"Something went wrong: {e}", []
        st.markdown(answer)
        if sources:
            with st.expander("Sources"):
                for s in sources:
                    st.write(f"📄 {s['source']}, page {s['page']}")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "sources": sources}
    )