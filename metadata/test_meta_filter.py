from embedding.embedding_generator import generate_embedding
from vectorstore.vector_store import FAISSStore
from metadata.meta_filter import filter_results
from utils.logger import log
import numpy as np

chunks = [
    "LCMS analysis showed high purity for MOL01234.",
    "Unexpected impurity observed during synthesis.",
    "HPLC results confirmed compound stability."
]

metadatas = [
    {"molecule_id": "MOL01234", "document_type": "experiment", "confidence_level": "validated"},
    {"molecule_id": "MOL01234", "document_type": "lab_notebook", "confidence_level": "exploratory"},
    {"molecule_id": "MOL04567", "document_type": "experiment", "confidence_level": "validated"}
]

def run_metadata_pipeline():
    embeddings = np.asarray(generate_embedding(chunks))

    if embeddings.ndim != 2:
        raise ValueError(f"Invalid embeddings shape: {embeddings.shape}")

    store = FAISSStore(embedding_dim=embeddings.shape[1])
    store.add_embeddings(embeddings, chunks, metadatas)

    query = "impurity found during experiment"
    query_embedding = generate_embedding([query])[0]

    results = store.search(query_embedding, top_k=5)

    filters = {
        "molecule_id": "MOL01234",
        "confidence_level": "validated"
    }

    filtered_results = filter_results(results, filters)

    for r in filtered_results:
        print(r)

    log("metadata filter test completed successfully")

if __name__ == "__main__":
    run_metadata_pipeline()
