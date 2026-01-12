from utils.logger import log  
from  utils.exception import  handle_exception
import os
from data_ingesction.experiment_ingesction.experimrnt_chunks  import  chunk_text


def detect_experiment_type(file_path):
    filename=os.path.basename(file_path).lower()

    if  "lcms" in filename:
        return "lcms"
    elif "nmr" in filename:
        return "NMR"
    elif "hplc" in  filename:
        return "HPLC"
    else :
        return "unknown"
    
def ingest_experiment(file_path):
    try:
        log(f"starting  experiment ingestion:{file_path}")

        with open(file_path, "r",encoding="utf-8") as f:
            text=f.read()

        if  not text.strip():
            raise ValueError("empty  experiment file")
        
        experiment_type=detect_experiment_type(file_path)

        chunks=chunk_text(text,chunk_size=500)

        log(f"experiment ingestion succesful;{file_path}")
        log(f"type={experiment_type}")

        return  {
            "chunks":chunks,
            "experiment_type":experiment_type
        }
    except Exception as e:
        handle_exception("experimrnt ingestion ",e)
        return  None
    
