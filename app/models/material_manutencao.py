from __future__ import annotations
from sqlalchemy import String, Integer, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship
from app.models.core import BaseColumns

class MaterialManutencao(BaseColumns):
    __tablename__ = "materiais_manutencao"
    manutencao_id: Mapped[int] = mapped_column(
        ForeignKey("manutencoes.id"), nullable=False
    )
    material_id: Mapped[int] = mapped_column(
        ForeignKey("materiais_estoque.id"), nullable=False
    )
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)
    preco_unitario: Mapped[float] = mapped_column(Float, nullable=False)
    custo: Mapped[float] = mapped_column(Float, nullable=False)
    manutencao = relationship("Manutencao", back_populates="materiais")
    material = relationship("MaterialEstoque")
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
