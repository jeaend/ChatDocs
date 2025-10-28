# ChatDocs for Loop  

**ChatDocs for Loop** is a local AI assistant that helps developers, contributors, and users navigate the open-source [Loop](https://github.com/LoopKit/Loop) diabetes management app documentation.  
It combines **local embeddings** and **Gemini 2.5 Flash** to deliver accurate, grounded answers -> and tells you when something isn’t in the docs.


## 🌟 Why This Project

Loop is a powerful open-source app that helps people with diabetes automate insulin delivery.  
However, its documentation and codebase can be complex to navigate — especially for newcomers.  

**ChatDocs** was built to bridge that gap: a **local, Gemini-powered assistant** that helps developers and contributors explore the Loop documentation and repositories conversationally.

This project demonstrates:
- Practical application of **LLMs (Gemini)** for technical documentation understanding  
- Implementation of a **Retrieval-Augmented Generation (RAG)** pipeline  
- Thoughtful UX for **developer productivity and knowledge exploration** using Makefile  

  
## Demo

<p align="center">
  <a href="https://github.com/jeaend/ChatDocs/raw/main/assets/chatdoc_demo.webm">
    <img src="https://private-user-images.githubusercontent.com/88771945/506703678-759c6580-d475-4a50-8346-2c769c592931.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjE2NzQxNDIsIm5iZiI6MTc2MTY3Mzg0MiwicGF0aCI6Ii84ODc3MTk0NS81MDY3MDM2NzgtNzU5YzY1ODAtZDQ3NS00YTUwLTgzNDYtMmM3NjljNTkyOTMxLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEwMjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMDI4VDE3NTA0MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFmYjQ0ZTVhYzE1NDc4OTIzN2RjNDFiYTgzZWIzNzExYTk5OWNkMTNlNTJmYjQ3ZWYyNTU2NWNlODE1OGNlM2ImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.huHoru0DfbznEaWn2vCwLSXbOblv5gNs8wpQwXqney8" width="75%" alt="ChatDocs Demo"/>
  </a>
</p>


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

## 🧩 Architecture

             ┌───────────────────────┐
             │  LoopDocs Markdown    │
             └────────────┬──────────┘
                          │
                   Load & Split Docs
                          │
               Embed with HuggingFace
                          │
                  Store in Chroma DB
                          │
                     Retrieve Context
                          │
        ┌─────────────────┴─────────────────┐
        │      ChatGoogleGenerativeAI       │
        │         (Gemini 2.5 Flash)        │
        └─────────────────┬─────────────────┘
                          │
                     Streamlit Chat UI


### 🧰 Developer Commands

| Command             | Description                                         |
| ------------------- | --------------------------------------------------- |
| `make check-gemini` | Verify your Gemini API key and accessible models    |
| `make setup`        | Create virtual environment and install dependencies |
| `make refresh`      | Pull latest LoopDocs and rebuild embeddings         |
| `make inspect`      | Inspect Chroma vector database                      |
| `make chat`         | Start ChatDocs in CLI mode                          |
| `make run-ui`       | Launch Streamlit web app                            |

## 🛠️ Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/jeaend/ChatDocs.git
cd ChatDocs
```

### 2️⃣ Create the environment
```bash
make setup
```

### 3️⃣ Add your Gemini API key, see the example .env file for guidance
Create a `.env` file in the root:
```bash
GOOGLE_API_KEY=your_gemini_api_key
```
You can get a key at [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

### 4️⃣ Verify Gemini access
```bash
make check-gemini
```

### 5️⃣ Build the vector store
```bash
make refresh
```

### 6️⃣ Start chatting
**CLI version**
```bash
make chat
```

**Streamlit UI**
```bash
make run-ui
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

## 🧠 Future Enhancements

- Multi-source documentation support (adding source code)
- Deployment to Streamlit Cloud / Hugging Face Spaces  
- Option to switch between Gemini, OpenAI, and Claude  

---


### 👋 Author

*Jeanne Endres* - 
Data Science & Software Engineer  
[LinkedIn](https://linkedin.com/in/jeanneendres) | [GitHub](https://github.com/jeaend) | [Website](https://jeaend.github.io) 
