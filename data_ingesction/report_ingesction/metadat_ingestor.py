from data_ingesction.report_ingesction.ingest_chunk import chunk_text
from  utils.logger  import  log
from  utils.exception import  handle_exception
import os 
from metadata.metadata_extract import build_metadata

def  ingest_report(file_path):
    try:
        log(f"starting the report  ingestion:{file_path}")

        with  open (file_path,"r",encoding="utf-8") as f:
            text=f.read()

            if not  text.strip():
                raise ValueError("empty file")
            
            chunks=chunk_text(text,text_size=500)

            metadata=build_metadata(
                text=text,
                source_type="report",
                source_file=os.path.basename(file_path)

            )

            log(f"report ingesdtion, chunking, metadata completed:{file_path}")

            return  {
                "chunks":chunks,
                "metadata":metadata
            }
    except Exception as e:
        handle_exception ("report ingestion",e)
        return None
log("metadata ingestor  has  completed")