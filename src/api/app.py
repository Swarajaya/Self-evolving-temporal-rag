from fastapi import FastAPI
from .schemas import QueryRequest, QueryResponse
from src.orchestration.langgraph_flow import flow

app = FastAPI(title="Self-Evolving Temporal RAG")

@app.post("/query", response_model=QueryResponse)
def query_rag(req: QueryRequest):
    result = flow(
        req.query,
        pipeline_fn=run_pipeline,
        controller=controller,
        source_dir="data/raw"
    )
    return result
