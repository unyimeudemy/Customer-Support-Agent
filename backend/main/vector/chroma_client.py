import os
import chromadb
from main.vector.onnx_embedder import ONNXEmbeddingFunction

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_STORE_PATH = os.path.join(BASE_DIR, "chroma_store")

# Initialize embedder
embedder = ONNXEmbeddingFunction()

# Make sure store directory exists (but don't delete)
os.makedirs(CHROMA_STORE_PATH, exist_ok=True)

# Start Chroma client
client = chromadb.PersistentClient(path=CHROMA_STORE_PATH)

# Get or create collection safely
collection = client.get_or_create_collection(name="my_collection", embedding_function=embedder)
