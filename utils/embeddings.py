import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

from config import (
    EMBEDDING_MODEL,
    VECTOR_STORE_PATH,
)

# Load embedding model
embedding_model = SentenceTransformer(EMBEDDING_MODEL)


def create_embeddings(documents):
    """
    Convert documents into embeddings.
    """

    texts = [doc["content"] for doc in documents]

    embeddings = embedding_model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True,
    )

    return embeddings


def save_vector_store(documents):

    embeddings = create_embeddings(documents)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    VECTOR_STORE_PATH.mkdir(exist_ok=True)

    faiss.write_index(
        index,
        str(VECTOR_STORE_PATH / "faiss_index.bin"),
    )

    with open(
        VECTOR_STORE_PATH / "metadata.pkl",
        "wb",
    ) as f:

        pickle.dump(documents, f)


def load_vector_store():

    index = faiss.read_index(
        str(VECTOR_STORE_PATH / "faiss_index.bin")
    )

    with open(
        VECTOR_STORE_PATH / "metadata.pkl",
        "rb",
    ) as f:

        metadata = pickle.load(f)

    return index, metadata


def search(query, top_k=3):

    index, metadata = load_vector_store()

    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True,
    )

    distances, indices = index.search(
        query_embedding,
        top_k,
    )

    results = []

    for idx in indices[0]:

        results.append(metadata[idx])

    return results