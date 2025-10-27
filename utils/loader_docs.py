import os
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma  

def load_and_embed_docs(
    docs_path="docs/",
    persist_dir="data/loopdocs/",
    chunk_size=1000,
    chunk_overlap=200,
):
    """
    Load LoopDocs markdown files, embed them using HuggingFace,
    and store the embeddings locally in a Chroma vector database.
    """

    if not os.path.exists(docs_path):
        raise FileNotFoundError(
            f"{docs_path} not found. Clone https://github.com/LoopKit/loopdocs.git first."
        )

    print("1: Loading LoopDocs markdowns...")
    loader = DirectoryLoader(docs_path, glob="**/*.md")
    documents = loader.load()
    print(f"✅ Loaded {len(documents)} documents.")

    # Split long documents into manageable chunks
    print("2: Splitting documents...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs_split = splitter.split_documents(documents)
    print(f"✅ Created {len(docs_split)} text chunks.")

    # Embed using HugginFace embeddings
    print("3: Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    print(f"✅ Embedding created.")

    print("4: Saving to Chroma vector store...")
    db = Chroma.from_documents(docs_split, embedding=embeddings, persist_directory=persist_dir)
    print(f"✅ Vector store saved in {persist_dir}")

    return db

if __name__ == "__main__":
    load_and_embed_docs()
