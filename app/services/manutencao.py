from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.manutencao import Manutencao
from app.models.material import Material
from app.schemas.manutencao import ManutencaoCreate


def get_by_id(db: Session, id: int) -> Manutencao | None:
    return db.scalar(select(Manutencao).where(Manutencao.id == id))

def get_all(db: Session) -> list[Manutencao]:
    return db.scalars(select(Manutencao)).all()

def create(db: Session, schema: ManutencaoCreate) -> Manutencao:
    db_obj = Manutencao(**schema.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def add_material(db: Session,manutencao_id: int,data: ManutencaoCreate) -> Manutencao:
    manutencao = db.get(Manutencao, manutencao_id)
    if not manutencao:
        raise ValueError("Manutenção não encontrada")
    material = Material(
        nome=data.nome,
        quantidade=data.quantidade,
        preco_unitario=data.preco_unitario,
        custo=data.quantidade * data.preco_unitario,
        manutencao=manutencao
    )
    db.add(material)
    db.commit()
    db.refresh(manutencao)

    return manutencao

def remove_material(db: Session, manutencao_id: int, material_id: int) -> Manutencao:
    manutencao = db.get(Manutencao, manutencao_id)
    if not manutencao:
        raise ValueError("Manutenção não encontrada")
    material = next(
        (m for m in manutencao.materiais if m.id == material_id),
        None
    )
    if not material:
        raise ValueError("Material não encontrado nesta manutenção")
    db.delete(material)
    db.commit()
    db.refresh(manutencao)

    return manutencao