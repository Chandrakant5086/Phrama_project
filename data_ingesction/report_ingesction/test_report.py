from data_ingesction.report_ingesction.report_ingstor import ingest_report
from utils.logger import  log 

log("testing  the repport  data file")
result=ingest_report("data/raw/reports/MOL00001_report_1.txt")

if result:
    print("ingestion ok ")
else:
    print("ingestion failed")
log ("tested  succesfully")