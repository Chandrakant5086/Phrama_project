from utils.logger import log
import os
import requests

OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL = "nomic-embed-text"

def generate_embedding(chunks):
    if not chunks:
        raise ValueError("No input chunks provided")

    # ✅ CI MOCK (MANDATORY)
    if os.getenv("CI") == "true":
        log("CI environment detected – using mock embeddings")
        return [[0.0] * 768 for _ in chunks]

    log("started embedding generation using Ollama")
    embeddings = []

    for text in chunks:
        if not text or not text.strip():
            raise ValueError("Empty text chunk found")

        try:
            response = requests.post(
                f"{OLLAMA_URL}/api/embeddings",
                json={
                    "model": OLLAMA_MODEL,
                    "prompt": text
                },
                timeout=30
            )
            response.raise_for_status()
            data = response.json()

        except Exception as e:
            raise RuntimeError(f"Ollama embedding call failed: {e}")

        if "embedding" not in data:
            raise RuntimeError("No embedding returned from Ollama")

        embeddings.append(data["embedding"])

    log(f"generated embeddings for {len(embeddings)} chunks")
    return embeddings




