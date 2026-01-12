from embedding.embedding_generator import generate_embedding
from vectorstore.vector_store import FAISSStore
from metadata.meta_filter import filter_results
from Reranker.ml_ranker import rerank_results
from typing import List, Dict


metadata = [
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
            "molecule_id": "MOL01234",
            "document_type": "experiment",
            "confidence_level": "validated"
        }
    ]





chunks = [
    "LCMS analysis showed high purity for MOL01234.",
    "Notebook notes mention impurity but not confirmed.",
    "HPLC confirmed compound stability."
]


embeddings=generate_embedding(chunks)

store=FAISSStore(embedding_dim=embeddings.shape[1])
store.add_embeddings(embeddings,chunks,metadata)

query_embedding=generate_embedding(["impurity analysis"])[0]
results=store.search(query_embedding,top_k=5)
filtered=filter_results(results,{"molecule_id":"MOL01234"})
reranked=rerank_results(filtered)

for  r in reranked:
    print(r["score"],r["metadata"]["document_type"])