from utils.logger import  log 
from  utils.exception import  handle_exception
import requests

OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL = "nomic-embed-text"   

def generate_embedding(chunks):
    try:
        log("started embedding generation using Ollama")

        embeddings = []

        for text in chunks:
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

        if "embedding" not in data:
            raise ValueError("No embedding returned from Ollama")

        embeddings.append(data["embedding"])

        log(f"generated embeddings for {len(chunks)} chunks")
        print(type(embeddings))

        return embeddings

    except Exception as e:
      print("EMBEDDING ERROR:", e)
      



