from typing import Annotated

from fastapi import APIRouter, Depends

from app.models import PublisherDTO, NewPublisherDTO
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

@publisher_router.put('', response_model=PublisherDTO)
async def update_publisher(
        publisher_service: Annotated[PublisherService, Depends(PublisherService)],
        publisher_name: str,
        new_publisher_dto: NewPublisherDTO,
) -> NewPublisherDTO:
    return publisher_service.update_publisher(publisher_name,new_publisher_dto)

@publisher_router.delete('', response_model=str)
async def delete_publisher(
        publisher_service: Annotated[PublisherService, Depends(PublisherService)],
        publisher_name: str
) -> str:
    return publisher_service.delete_publisher(publisher_name)