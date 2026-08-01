from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline,
)

from config import LLM_MODEL


# -----------------------------
# Load Local LLM
# -----------------------------

tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)

model = AutoModelForCausalLM.from_pretrained(
    LLM_MODEL,
    device_map="auto",
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)


# -----------------------------
# Prompt
# -----------------------------

TRIAGE_PROMPT = """
You are an OrbitDesk support classifier.

Choose ONLY one category.

1. answerable
2. requires_clarification
3. requires_escalation
4. out_of_scope

Rules

- If documentation can answer -> answerable
- If information is missing -> requires_clarification
- If user already performed documented troubleshooting and escalation is required -> requires_escalation
- Refunds, legal advice, billing actions or unrelated questions -> out_of_scope

Return ONLY the category.
"""


# -----------------------------
# Triage Node
# -----------------------------

def triage_node(state):

    question = state["question"]

    prompt = f"""
{TRIAGE_PROMPT}

Question:
{question}

Category:
"""

    result = generator(
        prompt,
        max_new_tokens=10,
        temperature=0,
    )

    prediction = result[0]["generated_text"].split("Category:")[-1]

    prediction = prediction.strip().lower()

    valid = [
        "answerable",
        "requires_clarification",
        "requires_escalation",
        "out_of_scope",
    ]

    classification = "requires_clarification"

    for item in valid:
        if item in prediction:
            classification = item
            break

    state["classification"] = classification

    return state