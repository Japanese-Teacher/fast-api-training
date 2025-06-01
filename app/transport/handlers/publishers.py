from typing import Annotated

from fastapi import APIRouter, Depends

from app.models import PublisherDTO
from app.services.publisher_service import PublisherService

publisher_router = APIRouter(
    prefix="/publishers",
    tags=["Publishers"],
)


@publisher_router.get('', response_model=list[PublisherDTO])
async def get_publishers(
        publisher_service: Annotated[PublisherService, Depends(PublisherService)],
) -> list[PublisherDTO]:
    return publisher_service.get_publishers()


@publisher_router.post('', response_model=PublisherDTO)
async def add_publisher(
        publisher_service: Annotated[PublisherService, Depends(PublisherService)],
        publisher_dto: PublisherDTO
) -> PublisherDTO:
    return publisher_service.add_publisher(publisher_dto)
