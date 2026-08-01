import json

from graph import graph


def main():

    print("=" * 60)
    print("OrbitDesk AI Support Agent")
    print("=" * 60)

    question = input("\nAsk your question:\n> ")

    initial_state = {

        "question": question,

        "classification": "",

        "retrieved_docs": [],

        "answer": "",

        "sources": [],

        "confidence": 0.0,

        "verified": False,

        "retry_count": 0,

        "reason": "",

        "requires_human": False,

        "clarification_question": "",

        "warnings": []

    }

    result = graph.invoke(initial_state)

    response = {
        "classification": result.get("classification"),
        "answer": result.get("answer"),
        "confidence": result.get("confidence"),
        "verified": result.get("verified"),
        "requires_human": result.get("requires_human"),
        "reason": result.get("reason"),
        "sources": [
            {
                "source_id": source["source_id"],
                "type": source["type"]
            }
            for source in result.get("sources", [])
        ]
    }

    print("\n" + "=" * 60)
    print("FINAL RESPONSE")
    print("=" * 60)

    print(json.dumps(response, indent=4))


if __name__ == "__main__":
    main()