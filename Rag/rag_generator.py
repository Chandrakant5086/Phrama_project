from utils.logger import  log
from utils.exception import handle_exception

from utils.logger import log
from utils.exception import handle_exception

def generate_answer(query, reranked_results, decision):
    """Generate final grounded answer using retrieved context"""

    log("Starting RAG answer generation")

    if decision == "REFUSE":
        return {
            "answer": "Insufficient validated information to provide a reliable answer.",
            "citations": []
        }

    context_chunks = []
    citations = []

    for item in reranked_results[:3]:
        context_chunks.append(item["chunk"])
        citations.append(item["metadata"])

    # Simple grounded answer (LLM placeholder)
    answer = (
        f"Based on internal research data: {query.lower()}\n\n"
        "Key findings:\n"
    )

    for chunk in context_chunks:
        answer += f"- {chunk}\n"

    if decision == "ANSWER_WITH_WARNING":
        answer += (
            "\n⚠️ Note: Some information is based on exploratory data "
            "and should be interpreted with caution."
        )

    log("RAG answer generation completed")

    return {
        "answer": answer,
        "citations": citations
    }
