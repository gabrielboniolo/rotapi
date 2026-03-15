from fastapi import APIRouter
from app.schemas import DistanciaInput, DistanciaOutput
from app.services.haversine import haversine_distance

router = APIRouter(prefix="/calcular", tags=["Calcular Distância"])


@router.post("/", response_model=DistanciaOutput)
def calcular_distancia(payload: DistanciaInput):
    distancia = haversine_distance(
        payload.lat1, payload.lon1,
        payload.lat2, payload.lon2
    )

    return DistanciaOutput(distancia_km=round(distancia, 3))
