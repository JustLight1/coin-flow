from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.wallet import Wallet
from app.schemas.wallet import SWalletUpdate


class WalletService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _update_wallet(self, obj_db: Wallet, amount: float) -> Wallet:
        """Обновляет сумму кошелька."""
        obj_db.amount += amount
        self.session.add(obj_db)
        await self.session.commit()
        await self.session.refresh(obj_db)
        return obj_db

    async def deposit(self, obj_db: Wallet, obj_in: SWalletUpdate) -> Wallet:
        """Вносит средства на кошелек."""
        return await self._update_wallet(obj_db, obj_in.amount)

    async def withdraw(self, obj_db: Wallet, obj_in: SWalletUpdate) -> Wallet:
        """Снимает средства с кошелька."""
        if obj_db.amount < obj_in.amount:
            raise HTTPException(
                status_code=400,
                detail='Сумма списания не может превышать текущий баланс!'
            )
        return await self._update_wallet(obj_db, -obj_in.amount)
