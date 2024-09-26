from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.wallet import Wallet
from app.schemas.wallet import SWalletCreate, SWalletUpdate
from app.services.wallet import WalletService


class CRUDWallet(CRUDBase[
    Wallet,
    SWalletCreate,
    SWalletUpdate
]):

    async def deposit(
        self,
        obj_db: Wallet,
        obj_in: SWalletUpdate,
        session: AsyncSession
    ) -> Wallet:
        """Вносит средства на кошелек."""
        service = WalletService(session)
        return await service.deposit(obj_db, obj_in)

    async def withdraw(
        self,
        obj_db: Wallet,
        obj_in: SWalletUpdate,
        session: AsyncSession
    ) -> Wallet:
        """Снимает средства с кошелька."""
        service = WalletService(session)
        return await service.withdraw(obj_db, obj_in)


crud_wallet = CRUDWallet(Wallet)
