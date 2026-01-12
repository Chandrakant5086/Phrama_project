from data_ingesction.experiment_ingesction.experiment_ingestor import ingest_experiment
import json

file_path = "data/raw/experiments/HPLC_MOL00208_3.txt"

result = ingest_experiment(file_path)
if result:
    with  open ("data/proceed/exp.json","w") as f:
        json.dump(result,f)
    print("Experiment type:", result["experiment_type"])
    print("Chunks:", len(result["chunks"]))
else:
    print("EXPERIMENT INGESTION FAILED & saved failed")
