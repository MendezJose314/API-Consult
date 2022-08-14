import requests
import json
import urllib.parse


def consult(url):
    response = requests.get(url, params={'page': 1, 'limit': 20, 'search': []})
    print(response)
    if response.status_code == 200:
        print(response.text)
        print("Las propiedades fueron consultadas con exito.")
    elif response.status_code == 400:
        print("La consulta tiene formato invalido. ")
    elif response.status_code == 401:
        print("La llave es invalida o caduco")


if __name__ == "__main__":
    consulta = 'https://api.stagingeb.com/playground#/properties?'
    consult(consulta)
