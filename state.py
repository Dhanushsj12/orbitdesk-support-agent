from typing import TypedDict, List, Dict


class AgentState(TypedDict):
    # User Input
    question: str

    # Triage
    classification: str

    # Retrieval
    retrieved_docs: List[Dict]

    # Generation
    answer: str

    # Verification
    verified: bool

    # Confidence
    confidence: float

    # Human escalation
    requires_human: bool

    # Retry counter
    retry_count: int

    # Reason
    reason: str

    # Sources
    sources: List[Dict]

    # Clarification
    clarification_question: str

    # Warnings
    warnings: List[str]