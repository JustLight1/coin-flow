from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.wallet import crud_wallet
from app.models.wallet import Wallet
from app.schemas.wallet import SWalletUpdate


async def validate_uuid(wallet_uuid: str) -> UUID:
    """Проверяет тип wallet_uuid на соответствие UUID."""
    try:
        return UUID(wallet_uuid)
    except ValueError:
        raise HTTPException(status_code=404, detail='Некорректный UUID!')


async def check_wallet_exists(
    wallet_uuid: str,
    session: AsyncSession
) -> Wallet:
    """Проверяет, существует ли кошелек с указанным идентификатором."""
    await validate_uuid(wallet_uuid)
    wallet = await crud_wallet.get(wallet_uuid, session)
    if wallet is None:
        raise HTTPException(
            status_code=404,
            detail='Кошелек не найден!'
        )
    return wallet


async def check_wallet_amount(
    wallet_uuid: str,
    operation_type: SWalletUpdate,
    session: AsyncSession
) -> Wallet:
    """Проверяет какую операцию нужно провести."""
    wallet = await check_wallet_exists(wallet_uuid, session)
    if operation_type.operationType == "DEPOSIT":
        wallet = await crud_wallet.deposit(wallet, operation_type, session)
    elif operation_type.operationType == "WITHDRAW":
        wallet = await crud_wallet.withdraw(wallet, operation_type, session)
    return wallet
