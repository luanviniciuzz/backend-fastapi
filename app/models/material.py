from __future__ import annotations
from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship
from app.models.core import BaseColumns


class Material(BaseColumns):
    __tablename__ = "materiais"

    nome: Mapped[str] = mapped_column(String(255), nullable=False)
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)
    preco_unitario: Mapped[float] = mapped_column(Float, nullable=False)
    custo: Mapped[float] = mapped_column(Float, nullable=False)
    manutencao_id: Mapped[int] = mapped_column(
        ForeignKey("manutencoes.id"),
        nullable=True
    )
    manutencao: Mapped["Manutencao"] = relationship(
        back_populates="materiais"
    )