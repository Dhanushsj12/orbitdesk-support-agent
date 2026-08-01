from config import KB_PATH, CASES_PATH
from utils.loader import load_all_documents
from utils.embeddings import save_vector_store


def main():

    print("=" * 50)
    print("OrbitDesk Vector Index Builder")
    print("=" * 50)

    print("\nLoading Knowledge Base and Resolved Cases...")

    documents = load_all_documents(
        KB_PATH,
        CASES_PATH
    )

    print(f"Loaded {len(documents)} documents.")

    print("\nCreating Embeddings...")
    save_vector_store(documents)

    print("\nVector Store Created Successfully!")

    print("\nFiles Generated:")

    print("vector_store/faiss_index.bin")
    print("vector_store/metadata.pkl")

    print("\nBuild Completed Successfully!")


if __name__ == "__main__":
    main()