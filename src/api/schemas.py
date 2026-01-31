from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
    confidence: float
    self_evolved: bool
