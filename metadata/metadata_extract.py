import  re 
from  utils.logger  import log
log("buliding  the metadata  started")
def extract_molecule_id(text):
    match = re.search(r"MOL\d{5}", text)
    return match.group(0) if match else None


def build_metadata(text, source_type, experiment_type=None, source_file=None):
    """Build standardized metadata dictionary"""

    metadata = {
        "molecule_id": extract_molecule_id(text),
        "document_type": source_type,
        "experiment_type": experiment_type,
        "confidence_level": (
            "exploratory" if source_type == "lab_notebook" else "validated"
        ),
        "source_file": source_file
    }

    return metadata


log("Successfully built metadata module")


