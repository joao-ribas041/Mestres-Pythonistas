# Arquivo JSON
from importlib.resources import path
import json
from pathlib import Path

carros = [
    {"Marca": "Nissan", "Preço": 45.000, "Cor": "Azul"},
    {"Marca": "Ford", "Preço": 75.000, "Cor": "Verde"},
    {"Marca": "BMW", "Preço": 117.000, "Cor": "Amarelo"}
]

carros_json = json.dumps(carros)
Path('carros.json').write_text(carros_json)

arquivo_carro_json = Path('carros.json').read_text()
arquivo_json = json.loads(arquivo_carro_json)
print(arquivo_json[0]['Marca'] + ' ' + str(arquivo_json[0]['Preço']))
print(arquivo_json[1]['Marca'] + ' ' + str(arquivo_json[1]['Preço']))
