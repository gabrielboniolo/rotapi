from fastapi import FastAPI
from app.routers import calcular

app = FastAPI(
    title="API Secundária - Cálculo de Distância",
    version="1.0.0"
)

app.include_router(calcular.router)


@app.get("/")
def home():
    return {"mensagem": "API Secundária funcionando!"}

#uvicorn app.main:app --reload --port 9000