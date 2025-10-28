# === ChatDocs Automation ===
# Usage:
#   make refresh   → pulls latest LoopDocs + rebuilds embeddings
#   make run       → starts Streamlit app

PYTHON := .venv/bin/python
DOCS_DIR := docs
DATA_DIR := data/loopdocs

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

run:
	@echo "🚀 Launching ChatDocs Streamlit app..."
	$(PYTHON) -m streamlit run app.py
