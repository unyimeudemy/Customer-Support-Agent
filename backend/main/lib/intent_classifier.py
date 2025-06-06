from chromadb import PersistentClient
from main.vector.onnx_embedder import ONNXEmbeddingFunction
import os

current_dir = os.path.dirname(__file__)
chroma_store_path = os.path.abspath(os.path.join(current_dir, "../vector/chroma_store"))

"""
    Here we bind the embedding function with the existing data store in store
    so that we can perform operations on the data.
"""
client = PersistentClient(path=chroma_store_path)
embedder = ONNXEmbeddingFunction()
intent_collection = client.get_or_create_collection(
    name="intent_collection",
    embedding_function=embedder
)

def classify_intent(query: str, threshold: float = 0.05) -> str:
    """Query the vector store"""
    results = intent_collection.query(
        query_texts=[query],
        n_results=1  
    )

    # Extract top match
    top_distance = results["distances"][0][0]  
    top_metadata = results["metadatas"][0][0]

    # Convert distance to similarity
    similarity = 1 / (1 + top_distance)


    if similarity >= threshold:
        return top_metadata["intent"]
    return "OPEN_ENDED"




