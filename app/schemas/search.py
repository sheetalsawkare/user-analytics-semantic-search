from pydantic import BaseModel

class SearchResult(BaseModel):
    event_id: str
    user_id: str
    event: str
    similarity_score: float

class SearchResponse(BaseModel):
    query: str
    total_results: int
    results: list[SearchResult]
