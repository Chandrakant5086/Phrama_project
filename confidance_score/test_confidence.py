from Reranker.ml_ranker import rerank_results
from confidance_score.confi_score import calculate_confidence
from confidance_score.decision import make_decision

# Simulated reranked results
reranked_results = [
    {
        "score": 1.5,
        "chunk": "LCMS confirmed high purity.",
        "metadata": {"confidence_level": "validated"}
    },
    {
        "score": 1.2,
        "chunk": "HPLC showed stable compound.",
        "metadata": {"confidence_level": "validated"}
    },
    {
        "score": 0.6,
        "chunk": "Notebook notes suggest impurity.",
        "metadata": {"confidence_level": "exploratory"}
    }
]

confidence = calculate_confidence(reranked_results)
decision = make_decision(confidence)

print("Confidence:", confidence)
print("Decision:", decision)
