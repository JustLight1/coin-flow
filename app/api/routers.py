from fastapi import APIRouter

from app.api.endpoints import wallet_router


main_router = APIRouter(
    prefix='/api/v1'
)
main_router.include_router(
    wallet_router, prefix='/wallets', tags=['Кошелек']
)
