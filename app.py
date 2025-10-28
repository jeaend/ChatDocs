import streamlit as st
from dotenv import load_dotenv
import os

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

# --- Setup ---
load_dotenv()
st.set_page_config(page_title="💬 ChatDocs", layout="wide")

# --- Load vectorstore ---
persist_dir = "data/loopdocs"
model_name = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(model_name=model_name)
vectordb = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# --- Gemini LLM ---
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# --- UI ---
st.title("💬 ChatDocs")
st.caption("Ask questions about Loop")

if "history" not in st.session_state:
    st.session_state["history"] = []

query = st.chat_input("Ask your question about LoopDocs...")
if query:
    with st.spinner("Thinking..."):
        result = qa_chain.invoke({"query": query})
        st.session_state["history"].append((query, result))

# --- Chat history ---
for q, res in st.session_state["history"]:
    st.chat_message("user").write(q)
    st.chat_message("assistant").write(res["result"])
    with st.expander("📚 Sources"):
        for doc in res["source_documents"]:
            st.write("-", doc.metadata.get("source", "Unknown"))
