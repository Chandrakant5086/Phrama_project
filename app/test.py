from embedding.embedding_generator import generate_embedding
from vectorstore.vector_store import FAISSStore
from metadata.meta_filter import filter_results
from Reranker.ml_ranker import rerank_results
from confidance_score.confi_score import calculate_confidence
from confidance_score.decision import make_decision
from Rag.rag_generator import generate_answer



chunks = [
    "LCMS analysis showed high purity (99.2%) for MOL01234 with no significant impurity peaks.",
    "HPLC analysis confirmed compound stability for MOL01234 over 48 hours.",
    "Lab notebook notes suggest possible impurity formation during synthesis for MOL01234.",
    "LCMS analysis detected a minor impurity peak for MOL04567."
]

                
   
metadata = [
    {
        "molecule_id": "MOL01234",
        "document_type": "experiment",
        "confidence_level": "validated"
    },
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
print(type(embeddings))          # <class 'list'>
print(type(embeddings[0]))       # <class 'list'>

embedding_dim = len(embeddings[0])
store = FAISSStore(embedding_dim=embedding_dim)

store.add_embeddings(embeddings, metadata, chunks)



# --------------------------------------------------
# 2️⃣ Function to run ONE query end-to-end
# --------------------------------------------------

def run_query(query, molecule_id=None):

    query_embedding = generate_embedding([query])[0]
    results = store.search(query_embedding, top_k=5)

    filters = {}
    if molecule_id:
        filters["molecule_id"] = molecule_id

    filtered = filter_results(results, filters)

    if not filtered:
        return {
            "query": query,
            "decision": "REFUSE",
            "confidence": 0.0,
            "answer": "No internal data found for the given molecule ID.",
            "citations": []
        }

    reranked = rerank_results(filtered)
    confidence = calculate_confidence(reranked)
    decision = make_decision(confidence)
    response = generate_answer(query, reranked, decision)

    return {
        "query": query,
        "decision": decision,
        "confidence": confidence,
        "answer": response["answer"],
        "citations": response["citations"]
    }



# --------------------------------------------------
# 3️⃣ Run multiple DIFFERENT queries
# --------------------------------------------------

run_query(
    query="What did LCMS analysis show for MOL04567?",
    molecule_id="MOL04567"
)

run_query(
    query="What did LCMS analysis show for MOL01234?",
    molecule_id="MOL01234"
)

run_query(
    query="What do lab notebooks say about MOL01234?",
    molecule_id="MOL01234"
)

run_query(
    query="Will MOL01234 succeed in clinical trials?",
    molecule_id="MOL04567"
) 