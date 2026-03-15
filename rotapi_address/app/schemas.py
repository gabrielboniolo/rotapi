from pydantic import BaseModel

class EnderecoBase(BaseModel):
    cep: str

class EnderecoCreate(EnderecoBase):
    pass

class EnderecoUpdate(BaseModel):
    logradouro: str | None = None
    bairro: str | None = None
    cidade: str | None = None
    uf: str | None = None

class EnderecoResponse(EnderecoBase):
    id: int
    logradouro: str
    bairro: str
    cidade: str
    uf: str

    class Config:
        orm_mode = True
