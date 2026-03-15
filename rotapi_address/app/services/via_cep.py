import requests

def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resp = requests.get(url, timeout=5)

    if resp.status_code != 200:
        return None

    data = resp.json()
    if "erro" in data:
        return None

    return data
