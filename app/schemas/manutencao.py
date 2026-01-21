from app.schemas.core import CamelSchema
from datetime import datetime
from typing import List
from app.schemas.materialmanutencao import MaterialManutencaoSchema


class ManutencaoBase(CamelSchema):
    resumo: str
    status: str = "aberta"

class ManutencaoCreate(ManutencaoBase):
    pass

class ManutencaoSchema(ManutencaoBase):
    id: int
    created_at: datetime | None = None
    materiais: List[MaterialManutencaoSchema]
    total_cost: float
    # Candidate will add 'materials' and 'total_cost' here
