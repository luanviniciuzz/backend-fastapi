from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.core import get_db
from app.schemas.material import MaterialSchema, MaterialCreate
from app.services import material as service

router = APIRouter(prefix="/material", tags=["Material"])


@router.post("/", response_model=MaterialSchema)
def create_material(data: MaterialCreate, db: Session = Depends(get_db)):
    return service.create(db, data)

@router.get("/", response_model=list[MaterialSchema])
def get_all_material(db: Session = Depends(get_db)):
    objs = service.get_all(db)
    return objs

@router.get("/{id}", response_model=MaterialSchema)
def get_material(id: int, db: Session = Depends(get_db)):
    obj = service.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Material not found")
    return obj
