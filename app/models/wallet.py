from decimal import Decimal

from sqlalchemy import CheckConstraint, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Wallet(Base):
    amount: Mapped[Decimal] = mapped_column(
        Numeric(precision=10, scale=2), nullable=False, default=Decimal('0.0')
    )

    __table_args__ = (
        CheckConstraint('amount >= 0.0', name='check_amount_positive'),
    )
