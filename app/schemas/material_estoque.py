from app.schemas.core import CamelSchema
from datetime import datetime


class MateriaEstoquelBase(CamelSchema):
    nome: str
    quantidade: int
    preco_unitario: float


class MaterialEstoqueCreate(MateriaEstoquelBase):
    pass


class MaterialEstoqueSchema(MateriaEstoquelBase):
    id: int
    created_at: datetime
    custo: float
