from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.core import get_db
from app.schemas.manutencao import ManutencaoSchema, ManutencaoCreate
from app.schemas.material_manutencao import MaterialManutencaoCreate
from app.services import manutencao as service

router = APIRouter(prefix="/manutencao", tags=["Manutencao"])

@router.post("/", 
    response_model=ManutencaoSchema,
    summary="Cria um solicitação de manutenção"
)
def create_manutencao(data: ManutencaoCreate, db: Session = Depends(get_db)):
    return service.create(db, data)

@router.get("/",
    response_model=list[ManutencaoSchema],
    summary="Lista todas as solicitações de manutenção"
)
def get_all_manutencao(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get("/{id}",
    response_model=ManutencaoSchema,
    summary="Exibi uma solicitação de manutenção pelo 'id'"
)
def get_manutencao(id: int, db: Session = Depends(get_db)):
    manutencao = service.get_by_id(db, id)
    if not manutencao:
        raise HTTPException(status_code=404, detail="Manutencao not found")
    return manutencao

@router.post("/{manutencao_id}/materiais",
    response_model=ManutencaoSchema,
    summary="Adiciona um material do estoque na solicitação de manutenção"
)
def add_material_to_manutencao( manutencao_id: int, data: MaterialManutencaoCreate, db: Session = Depends(get_db)):
    return service.add_material(db, manutencao_id, data)