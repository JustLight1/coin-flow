from sqlalchemy import Float, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Wallet(Base):
    amount: Mapped[float] = mapped_column(Float, nullable=False, default=0)

    __table_args__ = (
        CheckConstraint('amount > 0.0', name='check_amount_positive'),
    )
