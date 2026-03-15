from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import Endereco
from app.database import SessionLocal
from app.services.via_cep import consultar_cep
from app.schemas.endereco import EnderecoCreate, EnderecoUpdate, EnderecoResponse

endereco_router = APIRouter(prefix="/endereco", tags=["Endereço"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@endereco_router.post("/", response_model=EnderecoResponse)
def criar_endereco(data: EnderecoCreate, db: Session = Depends(get_db)):
    via = consultar_cep(data.cep)

    if not via:
        raise HTTPException(status_code=404, detail="CEP inválido ou não encontrado")

    endereco = Endereco(
        cep=data.cep,
        logradouro=via["logradouro"],
        bairro=via["bairro"],
        cidade=via["localidade"],
        uf=via["uf"],
        latitude=None,   # opcional
        longitude=None
    )

    db.add(endereco)
    db.commit()
    db.refresh(endereco)

    return endereco


@endereco_router.get("/{id}", response_model=EnderecoResponse)
def obter_endereco(id: int, db: Session = Depends(get_db)):
    e = db.query(Endereco).filter(Endereco.id == id).first()
    if not e:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return e


@endereco_router.put("/{id}", response_model=EnderecoResponse)
def atualizar_endereco(id: int, data: EnderecoUpdate, db: Session = Depends(get_db)):
    endereco = db.query(Endereco).filter(Endereco.id == id).first()

    if not endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    for campo, valor in data.dict(exclude_unset=True).items():
        setattr(endereco, campo, valor)

    db.commit()
    db.refresh(endereco)
    return endereco


@endereco_router.delete("/{id}")
def deletar_endereco(id: int, db: Session = Depends(get_db)):
    endereco = db.query(Endereco).filter(Endereco.id == id).first()

    if not endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    db.delete(endereco)
    db.commit()

    return {"mensagem": "Endereço removido com sucesso"}
