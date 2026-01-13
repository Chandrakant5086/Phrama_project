from embedding.embedding_generator import generate_embedding
from utils.logger import log
import numpy as np

chunks = [
    "This molecule showed high stability in LCMS analysis.",
    "Unexpected impurity observed during synthesis."
]

embeddings = np.asarray(generate_embedding(chunks))

print("Embeddings shape:", embeddings.shape)

log("test embedding successfully")
