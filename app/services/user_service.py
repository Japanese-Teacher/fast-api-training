from typing import Annotated

from fastapi import Depends

from app.integrations.postgres.user_repository import UserRepository
from app.models import UserDTO, NewUserDTO


class UserService:
    def __init__(
            self,
            user_repository: Annotated[UserRepository, Depends(UserRepository)],
    ):
        self.user_repository = user_repository

    def get_users(self) -> list[UserDTO]:
        return self.user_repository.get_users()

    def add_user(
            self,
            user_dto: UserDTO,
    ) -> UserDTO:
        return self.user_repository.add_user(user_dto)

    def update_user(
            self,
            new_user_dto: NewUserDTO,
    ) -> NewUserDTO:
        return self.user_repository.update_user(new_user_dto)

    def delete_user(
            self,
            user_id: int
    ) -> str:
        return self.user_repository.delete_user(user_id)
