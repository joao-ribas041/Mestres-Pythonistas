from requests.auth import HTTPBasicAuth
import requests
resultado = requests.get('http://localhost:5000/login',auth=('Joao','123'))

print(resultado.json())

resultado_autores = requests.get('http://localhost:5000/autores',headers={'x-acess-token': resultado.json()['token']})

print(resultado_autores.json())


