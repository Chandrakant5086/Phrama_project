from data_ingesction.experiment_ingesction.experimrnt_chunks import chunk_text
from utils.logger import log
from utils.exception import handle_exception
from metadata.metadata_extract import build_metadata
import os

def detect_experiment_type(file_path):
    name = os.path.basename(file_path).lower()
    if "lcms" in name:
        return "LCMS"
    if "nmr" in name:
        return "NMR"
    if "hplc" in name:
        return "HPLC"
    return "UNKNOWN"


def ingest_experiment(file_path):
    try:
        log(f"Starting experiment ingestion: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        if not text.strip():
            raise ValueError("Empty experiment file")

        chunks = chunk_text(text, chunk_size=400)
        experiment_type = detect_experiment_type(file_path)

        metadata = build_metadata(
            text=text,
            source_type="experiment",
            experiment_type=experiment_type,
            source_file=os.path.basename(file_path)
        )

        log(f"Experiment ingestion & metadata completed: {file_path}")

        return {
            "chunks": chunks,
            "metadata": metadata
        }

    except Exception as e:
        handle_exception("Experiment Ingestion", e)
        return None
log("experimet metadata has ingested  succesfully")