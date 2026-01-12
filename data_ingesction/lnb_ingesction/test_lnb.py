from data_ingesction.lnb_ingesction.ingest_lnb import ingest_lnb
from utils.logger import log 
from  utils.exception import  handle_exception
import json
log('test  of the  lnb data on the one example ')

result=ingest_lnb("data/raw/lab_notebooks/LNB_2024_00002.txt")

if  result :
    with open("data/proceed/lnb.json","w") as f:
        json.dump(result,f)
    print("lnb instection  is succesful")
    print ("chunks",len(result["chunks"]))
    

else:
    print(" lnb excuation failed")

