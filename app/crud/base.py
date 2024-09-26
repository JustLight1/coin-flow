from typing import Generic, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Базовый класс для операций CRUD.

    Attributes:
        model (Type[ModelType]): Модель базы данных.
    """

    def __init__(
        self,
        model: Type[ModelType]
    ):
        self.model = model

    async def get(
            self,
            obj_id: str,
            session: AsyncSession,
    ) -> ModelType | None:
        """
        Получает объект по его идентификатору.

        Args:
            obj_id (int): Идентификатор объекта.
            session (AsyncSession): Асинхронная сессия SQLAlchemy.

        Returns:
            ModelType or None: Найденный объект или None, если не найден.
        """
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id
            )
        )
        return db_obj.scalars().first()

    async def create(
            self,
            obj_in: CreateSchemaType,
            session: AsyncSession,
    ) -> ModelType:
        """
        Создает новый объект модели в базе данных.

        Args:
            obj_in (CreateSchemaType): Данные для создания объекта.
            session (AsyncSession): Асинхронная сессия SQLAlchemy.

        Returns:
            ModelType: Созданный объект модели.
        """
        obj_in_data = obj_in.model_dump()
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj
