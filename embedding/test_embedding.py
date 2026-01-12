from embedding.embedding_generator import generate_embedding
from utils.logger import log


chunks = [
    "This molecule showed high stability in LCMS analysis.",
    "Unexpected impurity observed during synthesis."
]

embeddings = generate_embedding(chunks)

if embeddings is not None:
    print("Embeddings shape:", embeddings.shape)
log("test embedding succesfully")