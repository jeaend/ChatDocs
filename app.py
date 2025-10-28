import streamlit as st
from dotenv import load_dotenv
import os
import base64
from io import BytesIO
from PIL import Image, ImageDraw

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI


# --- Helper: convert image to base64 for inline HTML ---
def image_to_base64(image: Image.Image, format="PNG") -> str:
    buffer = BytesIO()
    image.save(buffer, format=format)
    return base64.b64encode(buffer.getvalue()).decode()


# --- Setup ---
load_dotenv()

# --- Favicon (Loop logo, circular crop - safe for all sizes) ---
favicon_path = "assets/loop_logo.png"
favicon = None
if os.path.exists(favicon_path):
    logo_img = Image.open(favicon_path).convert("RGBA")

    # Make square by padding the shorter side
    size = max(logo_img.size)
    square_logo = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    offset = ((size - logo_img.size[0]) // 2, (size - logo_img.size[1]) // 2)
    square_logo.paste(logo_img, offset)

    # Create circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Apply circular mask
    circular_logo = Image.new("RGBA", (size, size))
    circular_logo.paste(square_logo, (0, 0), mask)
    favicon = circular_logo

# --- Page config ---
st.set_page_config(
    page_title="ChatDocs for Loop",
    page_icon=favicon,
    layout="wide",
)


# --- Load vectorstore ---
persist_dir = "data/loopdocs"
model_name = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(model_name=model_name)
vectordb = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
retriever = vectordb.as_retriever(search_kwargs={"k": 3})


# --- Gemini LLM ---
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# --- Header styling ---
st.markdown("""
    <style>
        .header-container {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-top: 0.5rem; /* tightened spacing */
            margin-bottom: 0.5rem;
        }
        .header-container img {
            vertical-align: middle;
            margin-bottom: 0 !important;
        }
        .header-container h1 {
            font-weight: 700;
            margin: 0;
            padding: 10;
        }
        .block-container {
            padding-top: 1rem !important; /* reduce Streamlit’s default padding */
        }
    </style>
""", unsafe_allow_html=True)

# --- Header (logo inline with text) ---
if os.path.exists(favicon_path):
    logo_img = Image.open(favicon_path)
    logo_b64 = image_to_base64(logo_img)
    st.markdown(
        f"""
        <div class="header-container">
            <img src="data:image/png;base64,{logo_b64}" width="40">
            <h1>ChatDocs</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.title("ChatDocs")

st.caption("Ask questions about Loop — make sure to give as much context as possible. 🙂")


# --- Chat logic ---
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
