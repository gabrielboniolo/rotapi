from fastapi import APIRouter, HTTPException
from app.services.distancia_service import calcular_distancia

router = APIRouter(prefix="/distancia", tags=["Distância"])

@router.get("/")
def distancia(lat1: float, lon1: float, lat2: float, lon2: float):
    result = calcular_distancia(lat1, lon1, lat2, lon2)

    if not result:
        raise HTTPException(status_code=500, detail="Erro ao calcular distância")

    return result
