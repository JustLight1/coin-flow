from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_wallet_amount, check_wallet_exists
from app.core.db import get_async_session
from app.crud.wallet import crud_wallet
from app.schemas.wallet import SWalletCreate, SWalletDB, SWalletUpdate


router = APIRouter()


@router.get(
    '/{wallet_uuid}',
    response_model=SWalletDB,
    status_code=status.HTTP_200_OK
)
async def get_wallet(
    wallet_uuid: str,
    session: AsyncSession = Depends(get_async_session)
):
    """Получить данные кошелька."""
    return await check_wallet_exists(wallet_uuid, session)


@router.post(
    '/{wallet_uuid}/operation',
    response_model=SWalletDB,
    status_code=status.HTTP_201_CREATED
)
async def wallet_operation(
    wallet_uuid: str,
    operation_type: SWalletUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """Обновить баланс кошелька."""
    wallet = await check_wallet_amount(wallet_uuid, operation_type, session)
    return wallet


@router.post(
    '/',
    response_model=SWalletDB,
    status_code=status.HTTP_201_CREATED
)
async def create_new_wallet(
        wallet: SWalletCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Создать кошелек."""
    new_wallet = await crud_wallet.create(wallet, session)
    return new_wallet
