from __future__ import annotations
from sqlalchemy import String, Float, Column, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.core import BaseColumns
from typing import List
from sqlalchemy.ext.hybrid import hybrid_property


class Manutencao(BaseColumns):
    __tablename__ = "manutencoes"

    resumo: Mapped[str] = mapped_column(String(500))
    status: Mapped[str] = mapped_column(String(50), default="aberta")
    # In the challenge, candidate adds relationships here
    materiais: Mapped[List["MaterialManutencao"]] = relationship(
        "MaterialManutencao",
        back_populates="manutencao",
        cascade="all, delete-orphan"
    )
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    @hybrid_property
    def total_cost(self) -> float:
        return sum(material.custo for material in self.materiais)