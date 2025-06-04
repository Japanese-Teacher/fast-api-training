from typing import Annotated

from fastapi import APIRouter, Depends

from app.integrations.postgres.user_repository import UserRepository
from app.models import UserDTO, NewUserDTO
from app.services.user_service import UserService

user_router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@user_router.get('', response_model=list[UserDTO])
async def get_users(
        user_service: Annotated[UserService, Depends(UserService)],
        page: int,
        size: int,
) -> list[UserDTO]:
    return user_service.get_users(page, size)


@user_router.post('', response_model=UserDTO)
async def add_users(
        user_service: Annotated[UserRepository, Depends(UserRepository)],
        user_dto: UserDTO,
) -> UserDTO:
    return user_service.add_user(user_dto)


@user_router.put('', response_model=NewUserDTO)
async def update_user(
        user_service: Annotated[UserService, Depends(UserService)],
        new_user_dto: NewUserDTO,
) -> NewUserDTO:
    return user_service.update_user(new_user_dto)


@user_router.delete('', response_model=str)
async def delete_user(
        user_service: Annotated[UserService, Depends(UserService)],
        user_id: int,
) -> str:
    return user_service.delete_user(user_id)
