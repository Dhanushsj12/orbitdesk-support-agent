from pathlib import Path

# ===========================
# Project Paths
# ===========================

BASE_DIR = Path(__file__).resolve().parent

KB_PATH = BASE_DIR / "knowledge_base"

DATA_PATH = BASE_DIR / "data"

CASES_PATH = DATA_PATH / "resolved_cases.json"

QUESTIONS_PATH = DATA_PATH / "sample_questions.json"

SCHEMA_PATH = DATA_PATH / "output_schema.json"

VECTOR_STORE_PATH = BASE_DIR / "vector_store"

MODEL_CACHE = BASE_DIR / "models"

# ===========================
# Models
# ===========================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "microsoft/Phi-3-mini-4k-instruct"

# ===========================
# Retrieval
# ===========================

TOP_K = 3

# ===========================
# Generation
# ===========================

TEMPERATURE = 0.2

MAX_NEW_TOKENS = 512

# ===========================
# Graph
# ===========================

MAX_RETRIES = 1

# ===========================
# Logging
# ===========================

LOG_LEVEL = "INFO"