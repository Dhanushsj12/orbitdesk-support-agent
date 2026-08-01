from models.llm import generate
from config import MAX_RETRIES


VERIFICATION_PROMPT = """
You are an OrbitDesk Answer Verifier.

Check the answer using ONLY the supplied evidence.

Verify:

1. Is the answer supported by the evidence?
2. Are there hallucinations?
3. Does it follow the evidence?
4. Is the answer safe?

Return ONLY

PASS

or

FAIL
"""


def verifier_node(state):

    answer = state["answer"]

    docs = state["retrieved_docs"]

    evidence = ""

    for doc in docs:

        evidence += f"""

Source:
{doc['source_id']}

Content:
{doc['content']}

"""

    prompt = f"""
{VERIFICATION_PROMPT}

Evidence:

{evidence}

Answer:

{answer}

Result:
"""

    result = generate(prompt, 5)

    result = result.upper()

    if "PASS" in result:

        state["verified"] = True

        state["reason"] = "Answer verified successfully."

        print("[VERIFIER] PASS")

        return state

    print("[VERIFIER] FAIL")

    retries = state.get("retry_count", 0)

    if retries < MAX_RETRIES:

        state["retry_count"] = retries + 1

        state["verified"] = False

        state["reason"] = "Retrying generation."

    else:

        state["verified"] = False

        state["classification"] = "safe_failure"

        state["answer"] = (
            "I cannot answer this confidently using the available documentation."
        )

        state["reason"] = "Verification failed."

        state["requires_human"] = True

    return state