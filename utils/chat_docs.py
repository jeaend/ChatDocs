# chat_docs.py
import os
from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

def main():
    load_dotenv()
    persist_dir = "data/loopdocs"
    model_name = "sentence-transformers/all-MiniLM-L6-v2"

    # 1️⃣ Load embeddings + Chroma
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    vectordb = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    # 2️⃣ Setup Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
    )

    # 3️⃣ Create QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    print("💬 ChatDocs is ready! Type 'exit' to quit.\n")

    # 4️⃣ Interactive loop
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        res = qa_chain.invoke({"query": query})
        print("\n🤖 Answer:\n", res["result"])

        print("\n📚 Sources:")
        for doc in res["source_documents"]:
            print("-", doc.metadata.get("source", "Unknown"))
        print()

if __name__ == "__main__":
    main()
