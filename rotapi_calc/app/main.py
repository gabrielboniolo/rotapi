from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routers import calcular

app = FastAPI(
    title="API Secundária - Cálculo de Distância",
    version="1.0.0"
)

app.include_router(calcular.router)

@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/docs")