from utils.embeddings import search

query = input("Ask a question: ")

results = search(query, top_k=3)

print("\nRetrieved Documents")
print("=" * 50)

for i, doc in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("-" * 40)

    print("Source :", doc["source_id"])
    print("Type   :", doc["type"])

    if doc["type"] == "resolved_case":
        print("Status :", doc.get("status"))

    print("\nPreview:")
    print(doc["content"][:500])

print("\nDone.")