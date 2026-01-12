from utils.logger import log
from utils.exception import handle_exception
from data_ingesction.lnb_ingesction.lnb_chunk import chunk_text


def ingest_lnb(file_path):
    try:
        log(f"starting lnb  ingestion:{file_path}")

        with open(file_path,"r",encoding="utf-8")as f:
            text=f.read()
        if not text.strip():
            raise ValueError("Empty LNB file ")
        chunks=chunk_text(text,chunk_size=500)
        log("lnb ingestion  succesful")
        return {
            "chunks":chunks
        }
    except Exception as e:
        handle_exception("lnb",e)
        return None
    

