from utils.logger import  log
from utils.exception import handle_exception
from data_ingesction.report_ingesction.ingest_chunk import chunk_text
log ("the  ingestion  started")

def ingest_report(file_path):
    try:
        log(f"Starting report ingestion: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        if not text.strip():
            raise ValueError("Empty report file")
        log("chunking  started")

        
        chunks = chunk_text(text, chunk_size=500)

        log(f"Report ingestion and chunking completed: {file_path}")

        return {
            "chunks": chunks,
            "source_type": "report"
        }

    except Exception as e:
        handle_exception("Report Ingestion", e)
        return None

log("data ingesction  process completed ")