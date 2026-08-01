from typing import TypedDict, List, Dict


class AgentState(TypedDict):

    # User Question
    question: str

    # Classification
    classification: str

    # Retrieved Documents
    retrieved_docs: List[Dict]

    # Generated Answer
    answer: str

    # Sources Used
    sources: List[Dict]

    # Confidence Score
    confidence: float

    # Verification
    verified: bool

    # Retry Count
    retry_count: int

    # Verification Reason
    reason: str

    # Human Escalation
    requires_human: bool

    # Clarification Question
    clarification_question: str

    # Warnings
    warnings: List[str]