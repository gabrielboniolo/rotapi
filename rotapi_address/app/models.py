from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Endereco(Base):
    __tablename__ = "enderecos"

    id = Column(Integer, primary_key=True, index=True)
    cep = Column(String, index=True)
    logradouro = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    uf = Column(String)
    latitude = Column(Float)      # opcional
    longitude = Column(Float)     # opcional
