from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.material import Material
from app.schemas.material import MaterialCreate

def get_all(db: Session) -> list[Material]:
    return db.scalars(select(Material)).all()

def get_by_id(db: Session, id: int) -> Material | None:
    return db.scalar(select(Material).where(Material.id == id))

def create(db: Session, schema: MaterialCreate) -> Material:
    db_obj = Material(
        nome=schema.nome,
        quantidade=schema.quantidade,
        preco_unitario=schema.preco_unitario,
        custo=schema.quantidade * schema.preco_unitario,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
