from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.database import Base, engine
from app.routers import enderecos, distancia

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Principal - Endereços e Distância",
    version="1.0.0"
)

app.include_router(enderecos.router)
app.include_router(distancia.router)

@app.get("/")
def home():
    return RedirectResponse(url="/docs")
