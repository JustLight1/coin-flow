from decimal import Decimal
from enum import Enum

from pydantic import UUID4, BaseModel, ConfigDict, Field


class OperationType(str, Enum):
    """Типы операций."""
    deposit = 'DEPOSIT'
    withdraw = 'WITHDRAW'


class SWallet(BaseModel):
    """Базовая схема кошелька."""
    amount: Decimal = Field(..., gt=0, max_digits=10, decimal_places=2)


class SWalletCreate(SWallet):
    """Схема создания кошелька."""


class SWalletUpdate(SWalletCreate):
    """
    Схема обновления кошелька.
    """
    operationType: OperationType


class SWalletDB(SWallet):
    """
    Схема вывода данных кошелька.

    model_config (ConfigDict): Конфигурация схемы для сериализации объектов
    базы данных, а не только Python-словарь или JSON-объект.
    """
    id: UUID4
    model_config = ConfigDict(from_attributes=True)
