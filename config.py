from pathlib import Path

# ==============================
# Project Paths
# ==============================

BASE_DIR = Path(__file__).resolve().parent

KB_PATH = BASE_DIR / "knowledge_base"

CASES_PATH = BASE_DIR / "data" / "resolved_cases.json"

QUESTIONS_PATH = BASE_DIR / "data" / "sample_questions.json"

SCHEMA_PATH = BASE_DIR / "data" / "output_schema.json"

VECTOR_STORE_PATH = BASE_DIR / "vector_store"

# ==============================
# Embedding Model
# ==============================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==============================
# Local LLM
# ==============================

LLM_MODEL = "microsoft/Phi-3-mini-4k-instruct"

# You can later replace this with TinyLlama,
# Qwen2.5, SmolLM etc.

# ==============================
# Retrieval
# ==============================

TOP_K = 3

# ==============================
# Graph
# ==============================

MAX_RETRIES = 1

# ==============================
# Generation
# ==============================

TEMPERATURE = 0.2

MAX_NEW_TOKENS = 512