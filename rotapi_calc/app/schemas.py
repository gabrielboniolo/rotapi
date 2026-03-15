from pydantic import BaseModel

class DistanciaInput(BaseModel):
    lat1: float
    lon1: float
    lat2: float
    lon2: float

class DistanciaOutput(BaseModel):
    distancia_km: float
