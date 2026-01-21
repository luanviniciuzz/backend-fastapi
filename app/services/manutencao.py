from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.manutencao import Manutencao
from app.models.materialestoque import MaterialEstoque
from app.models.materialmanutencao import MaterialManutencao
from app.schemas.manutencao import ManutencaoCreate
from app.schemas.materialmanutencao import MaterialManutencaoSchema


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

def add_material(db: Session,manutencao_id: int, data: MaterialManutencaoSchema) -> Manutencao:

    manutencao = db.get(Manutencao, manutencao_id)
    if not manutencao:
        raise ValueError("Manutenção não encontrada")

    material = db.get(MaterialEstoque, data.material_id)
    if not material:
        raise ValueError("Material não encontrado")

    if material.quantidade < data.quantidade:
        raise ValueError("Quantidade insuficiente em estoque")
    
    material.quantidade -= data.quantidade
    material.custo -= data.quantidade * material.preco_unitario

    material_manutencao = MaterialManutencao(
        manutencao=manutencao,
        material=material,
        quantidade=data.quantidade,
        preco_unitario=material.preco_unitario,
        custo=data.quantidade * material.preco_unitario
    )

    db.add(material_manutencao)
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