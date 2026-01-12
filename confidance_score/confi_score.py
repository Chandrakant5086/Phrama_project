from utils.logger import  log 


from utils.logger import log

def calculate_confidence(reranked_results, top_k=5):
    log("Calculating confidence score")

    print("\n=== DEBUG: RERANKED RESULTS ENTERING CONFIDENCE SCORER ===")

    if not reranked_results:
        print("❌ reranked_results is EMPTY")
        return 0.0

    top_results = reranked_results[:top_k]

    total_score = 0.0
    validated_count = 0

    for item in top_results:
        print("ITEM:", item)

        metadata = item.get("metadata", {})
        score = item.get("score", 0)

        print("  score:", score)
        print("  confidence_level:", metadata.get("confidence_level"))

        if metadata.get("confidence_level") == "validated":
            validated_count += 1
            total_score += score
        else:
            total_score += score * 0.4

    print("validated_count:", validated_count)
    print("total_score:", total_score)

    if validated_count == 0:
        print("❌ NO validated sources → confidence = 0")
        return 0.0

    avg_score = total_score / len(top_results)
    validated_ratio = validated_count / len(top_results)

    final_confidence = avg_score * validated_ratio

    print("avg_score:", avg_score)
    print("validated_ratio:", validated_ratio)
    print("final_confidence:", final_confidence)

    return round(final_confidence, 2)
