import faiss
import numpy as np

from utils.logger import log
from utils.exception import handle_exception

log("the vector storing  code  running")
class FAISSStore:
    def __init__(self, embedding_dim: int):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata = []

    def add_embeddings(self, embeddings, metadatas, chunks):
        try:
            log(f"Adding {len(embeddings)} embeddings to FAISS")

            vectors = np.array(embeddings).astype("float32")


            # Safety check
            if vectors.shape[1] != self.embedding_dim:
                raise ValueError("Embedding dimension mismatch")

            self.index.add(vectors)

            for meta, chunk in zip(metadatas, chunks):
                self.metadata.append({
                    "metadata": meta,
                    "chunk": chunk
                })

            log("Embeddings added successfully")

        except Exception as e:
            handle_exception("FAISS Add Embeddings", e)

    def search(self, query_embedding, top_k: int = 5):
        try:
            query_vector = np.array([query_embedding], dtype="float32")

            distances, indices = self.index.search(query_vector, top_k)

            results = []
            for idx in indices[0]:
                if idx != -1 and idx < len(self.metadata):
                    results.append(self.metadata[idx])

            return results

        except Exception as e:
            handle_exception("FAISS Search", e)
            return []

log("vector store  completed")