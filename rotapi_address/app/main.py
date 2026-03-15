from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.database import Base, engine
from app.routers import endereco, distancia

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Principal - Endereços e Distância",
    version="1.0.0"
)

app.include_router(endereco.endereco_router)
app.include_router(distancia.router)

@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/docs")
