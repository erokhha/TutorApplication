# app/models/receipt.py
from datetime import datetime

from sqlalchemy import ForeignKey, Numeric, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Receipt(Base):
    __tablename__ = "receipts"

    id: Mapped[int] = mapped_column(primary_key=True)
    payment_id: Mapped[int] = mapped_column(
        ForeignKey("payments.id"),
        nullable=False
    )

    amount: Mapped[float] = mapped_column(Numeric, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    title: Mapped[str] = mapped_column(String, nullable=False)
    payer_name: Mapped[str] = mapped_column(String, nullable=False)
    receipt_url: Mapped[str] = mapped_column(String, nullable=False)

    payment = relationship("Payment")
