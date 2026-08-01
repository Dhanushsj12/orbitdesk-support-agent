from models.llm import generate
from config import MAX_RETRIES
from utils.logger import logger


VERIFICATION_PROMPT = """
You are the OrbitDesk Answer Verification System.

You MUST verify the generated answer ONLY using the supplied evidence.

Verification Rules:

1. Is the answer completely supported by the evidence?
2. Does it avoid hallucinations?
3. Does it avoid unsupported assumptions?
4. Does it remain within OrbitDesk documentation?
5. Is it safe for the user?

Return ONLY one word.

PASS

or

FAIL
"""


def verifier_node(state):
    """
    Verify whether the generated answer is supported
    by the retrieved evidence.
    """

    logger.info("Starting Verification Node...")

    # -------------------------
    # Rule-Based Validation
    # -------------------------

    if len(state.get("sources", [])) == 0:

        logger.warning("No sources found.")

        state["verified"] = False
        state["reason"] = "No supporting sources."

        return state

    if state.get("answer", "").strip() == "":

        logger.warning("Generated answer is empty.")

        state["verified"] = False
        state["reason"] = "Empty answer."

        return state

    # -------------------------
    # Build Evidence
    # -------------------------

    evidence = ""

    for doc in state["retrieved_docs"]:

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

Generated Answer:

{state['answer']}

Verification:
"""

    result = generate(prompt, 10)

    result = result.upper()

    # -------------------------
    # PASS
    # -------------------------

    if "PASS" in result:

        logger.info("Verification Passed.")

        state["verified"] = True
        state["reason"] = "Answer verified."

        return state

    # -------------------------
    # FAIL
    # -------------------------

    logger.warning("Verification Failed.")

    retries = state.get("retry_count", 0)

    if retries < MAX_RETRIES:

        state["retry_count"] = retries + 1

        state["verified"] = False

        state["reason"] = "Retry generation."

        logger.info(
            f"Retry Count : {state['retry_count']}"
        )

    else:

        state["verified"] = False

        state["requires_human"] = True

        state["classification"] = "safe_failure"

        state["answer"] = (
            "I cannot answer confidently using the available documentation."
        )

        state["reason"] = (
            "Verification failed after retry."
        )

        logger.error(
            "Verification failed after maximum retries."
        )

    return state