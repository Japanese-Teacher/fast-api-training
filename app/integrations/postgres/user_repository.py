from typing import Annotated

from fastapi import Depends
from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from app.models import UserDTO, NewUserDTO
from app.orm import UserORM
from app.transport.depends.db import get_session


class UserRepository:
    def __init__(
            self,
            session: Annotated[Session, Depends(get_session)]
    ):
        self._session = session

    def get_users(
            self,
            page: int,
            size: int,
    ) -> list[UserDTO]:
        offset_val = (page - 1) * size
        users_orm = self._session.execute(
            select(UserORM)
            .order_by(UserORM.id)
            .offset(offset_val)
            .limit(size)
        )
        users_dto = []
        for user_orm in users_orm.scalars().all():
            user_dto = UserDTO(
                id=user_orm.id,
                first_name=user_orm.first_name,
                second_name=user_orm.second_name,
                age=user_orm.age,
                login=user_orm.login,
                password_hash=user_orm.password_hash,
            )
            users_dto.append(user_dto)
        return users_dto

    def add_user(
            self,
            user_dto: UserDTO,
    ) -> UserDTO:
        self._session.add(
            UserORM(
                id=user_dto.id,
                first_name=user_dto.first_name,
                second_name=user_dto.second_name,
                age=user_dto.age,
                login=user_dto.login,
                password_hash=user_dto.password_hash,
            )
        )
        self._session.flush()
        return user_dto

    def update_user(
            self,
            new_user_dto: NewUserDTO,
    ) -> NewUserDTO:
        user_orm = self._session.get(UserORM, new_user_dto.id)
        if user_orm:
            user_orm.first_name = new_user_dto.new_first_name
            user_orm.second_name = new_user_dto.new_second_name
            user_orm.age = new_user_dto.new_age
            user_orm.login = new_user_dto.new_login
            user_orm.password_hash = new_user_dto.new_password_hash
            self._session.flush()
            self._session.refresh(user_orm)
        return new_user_dto

    def delete_user(
            self,
            user_id: int
    ) -> str:
        self._session.execute(delete(UserORM).where(UserORM.id == user_id))
        return 'Удаление успешно произведено'
