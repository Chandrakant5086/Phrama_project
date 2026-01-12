from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from app.test import run_query 

app = FastAPI(title="Pharma RAG API")

# ----------------------------
# Request schema
# ----------------------------

class QueryRequest(BaseModel):
    query: str
    molecule_id: Optional[str] = None


# ----------------------------
# REST endpoint
# ----------------------------
@app.post("/rag/query")
def rag_query(payload: QueryRequest):
    result = run_query(
        query=payload.query,
        molecule_id=payload.molecule_id
    )
    return result
