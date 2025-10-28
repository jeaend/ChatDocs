# === ChatDocs Automation ===
# Usage:
#   make check-gemini 	→ verify Google API key + Gemini access
#   make setup   		→ creates the virtual environment
#   make refresh   		→ pulls latest LoopDocs + rebuilds embeddings
#   make inspect   		→ inspect the Chroma vector database
#   make chat          	→ run the ChatDocs CLI
#   make run-ui       	→ launch the Streamlit ChatDocs web app


PYTHON := .venv/bin/python
DOCS_DIR := docs
DATA_DIR := data/loopdocs

.PHONY: check-gemini
check-gemini:
	@echo "🔍 Checking Gemini API key and accessible models..."
	@$(PYTHON) utils/check_gemini.py

setup:
	@echo "📦 Creating virtual environment..."
	python3 -m venv .venv
	@echo "📦 Installing dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	@echo "✅ Environment ready!"

refresh:
	@echo "🔄 Pulling latest LoopDocs..."
	cd docs && git pull origin main
	@echo "🧹 Cleaning old embeddings..."
	rm -rf data/loopdocs/
	@echo "🧠 Rebuilding embeddings..."
	$(PYTHON) -m utils.loader_docs
	@echo "✅ Refresh complete."

inspect:
	@echo "🔍 Inspecting Chroma database..."
	$(PYTHON) -m utils.inspect_vectors

run:
	@echo "🚀 Launching ChatDocs Streamlit app..."
	$(PYTHON) -m streamlit run app.py

chat:
	@echo "💬 Starting ChatDocs CLI..."
	$(PYTHON) -m utils.chat_docs

