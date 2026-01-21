from app.schemas.core import CamelSchema
from datetime import datetime


class MaterialBase(CamelSchema):
    nome: str
    quantidade: int
    preco_unitario: float


class MaterialCreate(MaterialBase):
    pass


class MaterialSchema(MaterialBase):
    id: int
    created_at: datetime | None = None
    custo: float
