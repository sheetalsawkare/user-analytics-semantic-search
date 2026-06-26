from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.services.search_service import SearchService
from app.schemas.search import SearchResponse

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

@router.get("",
    response_model=SearchResponse)

async def search(
        query: str,
        db: AsyncSession = Depends(get_db)
    ):

    return await SearchService.search(
        db=db,
        query=query
    )