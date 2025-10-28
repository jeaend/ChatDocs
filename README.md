# ChatDocs for Loop  

ChatDocs for Loop is a local AI assistant that helps developers, contributors and users navigate the open-source [Loop](https://github.com/LoopKit/Loop) iOS diabetes management app documentation.  
It runs entirely locally, using **Gemini** for reasoning and **LangChain** for intelligent retrieval.


## 🌟 Why This Project

Loop is a powerful open-source app that helps people with diabetes automate insulin delivery.  
However, its documentation and codebase can be complex to navigate; especially for newbies.  

**ChatDocs** was built to bridge that gap: a local, Gemini-powered assistant that helps developers and contributors explore the Loop documentation and repositories conversationally.

This project demonstrates:
- Practical application of **LLMs (Gemini)** for technical documentation understanding  
- Implementation of a **Retrieval-Augmented Generation (RAG)** pipeline over mixed sources (Markdown + code)  
- Thoughtful UX for **developer productivity and knowledge exploration**
  
## Demo

Coming soon — a short walkthrough showing ChatDocs exploring LoopDocs and LoopKit repositories.

---

## 🧠 Example Use Cases

- “Where does Loop define insulin delivery logic in code?”  
- “How do I configure a new CGM according to the LoopDocs?”  
- “What dependencies does the LoopKit framework have?”  
- “Explain how Loop handles carb entries.”

---

## Features

- **Ask questions across Loop’s entire ecosystem** — from user guides in LoopDocs to developer notes in the Loop and LoopKit repos.  
- **Context-aware answers powered by Gemini + LangChain**, combining human-readable docs and actual source code for deeper reasoning.  
- **Local and private** — all embeddings, retrieval, and chat run on your machine (no external API calls beyond Gemini).  
- **Transparent retrieval** — see which document or code file each answer came from.  
- **Multi-source knowledge base** — integrates Markdown docs, Swift files, and configuration schemas.  
- **Streamlit interface for developers** — simple, fast, and designed for documentation exploration.  
---

## 🧩 Tech Stack

| Component | Purpose |
|------------|----------|
| **Gemini API** | LLM reasoning and summarization |
| **LangChain** | Retrieval-Augmented Generation pipeline |
| **Chroma** | Local vector database for document embeddings |
| **Streamlit** | Interactive UI for chatting with docs |
| **Python** | Core logic and integration |

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/jeaend/ChatDocs.git
cd ChatDocs
```

### 🧰 Developer Commands

| Command | Description |
|----------|-------------|
| `make setup` | Create local Python environment |
| `make refresh` | Pull latest docs and rebuild embeddings |
| `make run` | Launch Streamlit app locally |

Usage
# 1. Setup once (creates .venv)
make setup

# 2. Rebuild embeddings and pull latest docs
make refresh

# 3. Run the Streamlit app
make run

### 2. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Add your Gemini API key
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```
You can get a key at [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the Streamlit URL (usually `http://localhost:8501`) to start chatting with the Loop docs.

---
## 📚 Project Structure

```
ChatDocs/
│
├── app.py              # Streamlit interface
├── config.py           # Environment and API key setup
├── requirements.txt
│
├── docs/               # LoopDocs markdown files
├── repos/              # Cloned LoopKit repositories
├── data/               # Local embeddings / vector indexes
│
└── utils/
    ├── loader_docs.py  # Loads LoopDocs
    ├── loader_code.py  # Loads and parses LoopKit repo files
    ├── embedder.py     # Embedding + Chroma store logic
    └── chat.py         # Retrieval + chat chain
```

---

### 👋 Author

*Jeanne Endres* - 
Data Science & Software Engineer  
[LinkedIn](https://linkedin.com/in/jeanneendres) | [GitHub](https://github.com/jeaend) | [Website](https://jeaend.github.io) 
