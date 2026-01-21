from app.schemas.core import CamelSchema
from datetime import datetime



class MaterialManutencaoBase(CamelSchema):
    material_id: int
    quantidade: int


class MaterialManutencaoCreate(MaterialManutencaoBase):
    pass


class MaterialManutencaoSchema(MaterialManutencaoBase):
    id: int
    preco_unitario: float
    custo: float
    created_at: datetime | None = None
