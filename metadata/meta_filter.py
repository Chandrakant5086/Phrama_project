from utils.logger import log

def filter_results(results, filters):
    log(f"Applying metadata filters: {filters}")

    filtered = []

    for item in results:
        metadata = item.get("metadata", {})

        # Molecule filter
        if "molecule_id" in filters:
            if metadata.get("molecule_id") != filters["molecule_id"]:
                continue

        # Document type filter
        if "document_type" in filters:
            if metadata.get("document_type") != filters["document_type"]:
                continue

        # Confidence level filter
        if "confidence_level" in filters:
            if metadata.get("confidence_level") != filters["confidence_level"]:
                continue

        filtered.append(item)

    log(f"Filtered results count: {len(filtered)}")
    return filtered


log("Metadata filter module loaded successfully")
