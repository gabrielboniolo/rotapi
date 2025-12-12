from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.services.via_cep import consultar_cep

router = APIRouter(prefix="/enderecos", tags=["Endereços"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST - Criar endereço usando ViaCEP
@router.post("/", response_model=schemas.EnderecoResponse)
def criar_endereco(data: schemas.EnderecoCreate, db: Session = Depends(get_db)):
    via = consultar_cep(data.cep)

    if not via:
        raise HTTPException(status_code=404, detail="CEP inválido ou não encontrado")

    endereco = models.Endereco(
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


# GET - Buscar por ID
@router.get("/{id}", response_model=schemas.EnderecoResponse)
def obter_endereco(id: int, db: Session = Depends(get_db)):
    e = db.query(models.Endereco).filter(models.Endereco.id == id).first()
    if not e:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return e


# PUT - Atualizar dados
@router.put("/{id}", response_model=schemas.EnderecoResponse)
def atualizar_endereco(id: int, data: schemas.EnderecoUpdate, db: Session = Depends(get_db)):
    endereco = db.query(models.Endereco).filter(models.Endereco.id == id).first()

    if not endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    for campo, valor in data.dict(exclude_unset=True).items():
        setattr(endereco, campo, valor)

    db.commit()
    db.refresh(endereco)
    return endereco


# DELETE - Remover endereço
@router.delete("/{id}")
def deletar_endereco(id: int, db: Session = Depends(get_db)):
    endereco = db.query(models.Endereco).filter(models.Endereco.id == id).first()

    if not endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    db.delete(endereco)
    db.commit()

    return {"mensagem": "Endereço removido com sucesso"}
