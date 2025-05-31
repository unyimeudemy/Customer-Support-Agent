# main/vector/onnx_embedder.py
from django.conf import settings
import os
import onnxruntime as ort
from transformers import AutoTokenizer
from chromadb.utils.embedding_functions import EmbeddingFunction
import numpy as np


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
EMBEDDINGS_DIR = os.path.join(PROJECT_ROOT, "embedded_onnx")

class ONNXEmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        model_path = os.path.join(EMBEDDINGS_DIR, "model.onnx")
        tokenizer_path = os.path.join(EMBEDDINGS_DIR, "tokenizer")
        self.session = ort.InferenceSession(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path, local_files_only=True)

    def __call__(self, texts):
        inputs = self.tokenizer(texts, return_tensors="np", padding=True, truncation=True)
        ort_inputs = {k: v for k, v in inputs.items()}
        outputs = self.session.run(None, ort_inputs)
        embeddings = np.mean(outputs[0], axis=1)

        return embeddings.tolist()