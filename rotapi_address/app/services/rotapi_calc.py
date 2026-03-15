import requests

API_SECUNDARIA_URL = "http://localhost:9000/calcular"  # ajuste quando criar o container

def calcular_distancia(lat1, lon1, lat2, lon2):
    payload = {
        "lat1": lat1,
        "lon1": lon1,
        "lat2": lat2,
        "lon2": lon2
    }

    response = requests.post(API_SECUNDARIA_URL, json=payload)

    if response.status_code != 200:
        return None

    return response.json()
