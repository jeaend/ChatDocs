"""
inspect_vectors.py
------------------
Inspect your Chroma vector database (for LoopDocs embeddings).
Displays how many chunks are stored, their metadata, and text previews.
"""

from langchain.vectorstores import Chroma


def inspect_chroma(persist_dir="data/loopdocs/", limit=5):
    print(f"🔍 Inspecting Chroma DB at: {persist_dir}")

    # Load the database
    db = Chroma(persist_directory=persist_dir)
    collection = db._collection

    count = collection.count()
    print(f"✅ Total vectors stored: {count}")

    # Peek at a few stored documents
    print(f"\n📄 Showing {limit} example chunks:\n")
    sample = collection.peek(limit)

    for i, (meta, text) in enumerate(zip(sample["metadatas"], sample["documents"]), 1):
        print(f"--- Chunk {i} ---")
        print("Source:", meta.get("source", "Unknown"))
        print("Text preview:", text[:250].replace('\n', ' '), "...")
        print()

    print("🧠 Done.")


if __name__ == "__main__":
    inspect_chroma()
