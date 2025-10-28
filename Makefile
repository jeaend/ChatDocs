# === ChatDocs Automation ===
# Usage:
#   make refresh   → pulls latest LoopDocs + rebuilds embeddings
#   make run       → starts Streamlit app

PYTHON := .venv/bin/python

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
