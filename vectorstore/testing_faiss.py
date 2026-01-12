from embedding.embedding_generator import generate_embedding
from vectorstore.vector_store import FAISSStore
from  utils.logger import log
log ("starting  the testing")
chunks = [
    "LCMS analysis showed high purity for MOL01234.",
    "Unexpected impurity observed during synthesis.",
    "HPLC results confirmed compound stability."
]

metadatas = [
    {"molecule_id": "MOL01234", "source": "experiment"},
    {"molecule_id": "MOL01234", "source": "lab_notebo"
    "ok"},
    {"molecule_id": "MOL04567", "source": "experiment"}
]

embeddings = generate_embedding(chunks)

store = FAISSStore(embedding_dim=embeddings.shape[1])
store.add_embeddings(embeddings, metadatas, chunks)

query = "impurity found during experiment"
query_embedding = generate_embedding([query])[0]

results = store.search(query_embedding, top_k=2)

for r in results:
    print(r)
log("succesfull testing  completed")