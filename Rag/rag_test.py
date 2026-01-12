from Reranker.ml_ranker import rerank_results
from confidance_score.confi_score import calculate_confidence
from confidance_score.decision import make_decision
from Rag.rag_generator import generate_answer



queary="LCMS analysis showed no significant impurities for MOL00208."

rerank_results=[
    {
        "score": 1.6,
        "chunk": "LCMS analysis showed no significant impurities for MOL01234.",
        "metadata": {"confidence_level": "validated", "source": "LCMS"}
    },
    {
        "score": 1.3,
        "chunk": "HPLC results confirmed compound stability.",
        "metadata": {"confidence_level": "validated", "source": "HPLC"}
    },
    {
        "score": 0.6,
        "chunk": "Notebook notes mention possible impurity under certain conditions.",
        "metadata": {"confidence_level": "exploratory", "source": "LNB"}
    }
]


confidence=calculate_confidence(rerank_results)
decision=make_decision(confidence)
response=generate_answer(queary,rerank_results,decision)

print ("decision",decision)
print("\n Answer: \n",response["answer"])
print("\n citation:")

for c in response["citations"]:
    print(c)