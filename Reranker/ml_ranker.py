from  utils.logger import  log



def rerank_results(results):
    reranked = []

    for item in results:
        metadata = item["metadata"]
        score = 0.0

        if metadata.get("confidence_level") == "validated":
            score += 1.0
        else:
            score += 0.4

        if metadata.get("document_type") == "experiment":
            score += 0.5
        elif metadata.get("document_type") == "report":
            score += 0.3
        elif metadata.get("document_type") == "lab_notebook":
            score += 0.1

        reranked.append({
            "score": score,
            "chunk": item["chunk"],
            "metadata": metadata
        })

    reranked.sort(key=lambda x: x["score"], reverse=True)
    return reranked
   
    






