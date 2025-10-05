from pathlib import Path
import os

# basic paths (you can tweak later via .env if you want)
RAW_DIR = Path(os.getenv("RAW_DIR", "./data/raw")).resolve()
INDEX_DIR = Path(os.getenv("INDEX_DIR", "./index/chroma")).resolve()
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "docqa")

# model names
EMBED_MODEL = os.getenv("EMBED_MODEL", "models/embedding-001")   # Google embeddings
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.0-flash")
