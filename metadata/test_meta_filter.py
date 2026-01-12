from embedding.embedding_generator import generate_embedding
from vectorstore.vector_store import FAISSStore
from metadata.meta_filter import filter_results
from utils.logger import  log

chunks = [
    "LCMS analysis showed high purity for MOL01234.",
    "Unexpected impurity observed during synthesis.",
    "HPLC results confirmed compound stability."
]

metadatas = [
    {
        "molecule_id": "MOL01234",
        "document_type": "experiment",
        "confidence_level": "validated"
    },
    {
        "molecule_id": "MOL01234",
        "document_type": "lab_notebook",
        "confidence_level": "exploratory"
    },
    {
        "molecule_id": "MOL04567",
        "document_type": "experiment",
        "confidence_level": "validated"
    }
]

embeddings = generate_embedding(chunks)

store = FAISSStore(embedding_dim=embeddings.shape[1])
store.add_embeddings(embeddings, metadatas, chunks)

query = "impurity found during experiment"
query_embedding = generate_embedding([query])[0]

results = store.search(query_embedding, top_k=5)

# Apply metadata filter
filters = {
    "molecule_id": "molecule_id",
    "confidence_level": "validated"
}

filtered_results = filter_results(results, filters)

for r in filtered_results:
    print(r)
log("tested the  metadata")