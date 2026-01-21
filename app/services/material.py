from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.materialestoque import MaterialEstoque
from app.schemas.materialestoque import MaterialEstoqueCreate

def get_all(db: Session) -> list[MaterialEstoque]:
    return db.scalars(select(MaterialEstoque)).all()

def get_by_id(db: Session, id: int) -> MaterialEstoque | None:
    return db.scalar(select(MaterialEstoque).where(MaterialEstoque.id == id))

def create(db: Session, schema: MaterialEstoqueCreate) -> MaterialEstoque:
    db_material_estoque = MaterialEstoque(
        nome=schema.nome,
        quantidade=schema.quantidade,
        preco_unitario=schema.preco_unitario,
        custo=schema.quantidade * schema.preco_unitario,
    )
    db.add(db_material_estoque)
    db.commit()
    db.refresh(db_material_estoque)
    return db_material_estoque
