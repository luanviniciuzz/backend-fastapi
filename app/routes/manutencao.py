from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.core import get_db
from app.schemas.manutencao import ManutencaoSchema, ManutencaoCreate
from app.schemas.materialmanutencao import MaterialManutencaoCreate
from app.services import manutencao as service

router = APIRouter(prefix="/manutencao", tags=["Manutencao"])

@router.post("/", response_model=ManutencaoSchema)
def create_manutencao(data: ManutencaoCreate, db: Session = Depends(get_db)):
    return service.create(db, data)

@router.get("/", response_model=list[ManutencaoSchema])
def get_all_manutencao(db: Session = Depends(get_db)):
    objs = service.get_all(db)
    return objs

@router.get("/{id}", response_model=ManutencaoSchema)
def get_manutencao(id: int, db: Session = Depends(get_db)):
    obj = service.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Manutencao not found")
    return obj

@router.post("/{manutencao_id}/materiais",response_model=ManutencaoSchema)
def add_material_to_manutencao( manutencao_id: int, data: MaterialManutencaoCreate, db: Session = Depends(get_db)):
    return service.add_material(db, manutencao_id, data)
    
@router.delete("/{manutencao_id}/materiais/{material_id}",response_model=ManutencaoSchema)
def remove_material_from_manutencao(manutencao_id: int, material_id: int, db: Session = Depends(get_db)):
    try:
        return service.remove_material(db, manutencao_id, material_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))