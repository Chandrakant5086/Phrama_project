from data_ingesction.lnb_ingesction.lnb_chunk import chunk_text
from utils.logger import log
from utils.exception import handle_exception
from metadata.metadata_extract import build_metadata
import os

def ingest_lnb(file_path):
    try:
        log(f"Starting LNB ingestion: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        if not text.strip():
            raise ValueError("Empty LNB file")

        chunks = chunk_text(text, chunk_size=300)

        metadata = build_metadata(
            text=text,
            source_type="lab_notebook",
            source_file=os.path.basename(file_path)
        )

        log(f"LNB ingestion & metadata completed: {file_path}")

        return {
            "chunks": chunks,
            "metadata": metadata
        }

    except Exception as e:
        handle_exception("LNB Ingestion", e)
        return None
log("lan  meata data  ingestion  has  completes successfully")