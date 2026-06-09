import requests


def buscar_autor_externo():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    response.raise_for_status()

    return response.json()