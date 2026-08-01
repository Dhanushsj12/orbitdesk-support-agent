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

    print("\n" + "=" * 60)
    print("FINAL RESPONSE")
    print("=" * 60)

    print("\nAnswer:")
    print(result["answer"])

    print("\nConfidence:")
    print(result["confidence"])

    print("\nVerified:")
    print(result["verified"])

    print("\nClassification:")
    print(result["classification"])

    print("\nSources:")

    for source in result["sources"]:

        print(
            f"- {source['source_id']} ({source['type']})"
        )


if __name__ == "__main__":
    main()