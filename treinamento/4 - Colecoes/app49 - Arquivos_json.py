# Arquivo JSON
from importlib.resources import path
import json
from pathlib import Path

# carros = [
#     {"Marca": "Nissan", "Preço": 45.000, "Cor": "Azul"},
#     {"Marca": "Ford", "Preço": 75.000, "Cor": "Verde"},
#     {"Marca": "BMW", "Preço": 117.000, "Cor": "Amarelo"}
# ]

# carros_json = json.dumps(carros)
# Path('carros.json').write_text(carros_json)

arquivo_carro_json = Path('carros.json').read_text()
arquivo_json = json.loads(arquivo_carro_json)
print(arquivo_json[0]['Marca'] + ' ' + str(arquivo_json[0]['Preço']))
print(arquivo_json[1]['Marca'] + ' ' + str(arquivo_json[1]['Preço']))


# Seu único desafio é de encontrar e exibir na tela a 'ability' 'lightning-rod'
# Esse é o único desafio
# Faça com calma, e depois veja como eu resolvi esse desafio
# Pode parecer simples, mas se ainda não se acostumou em navegar em dicionários, pode
# levar um tempo então vá com calma e depois volte aqui para ver o resultado

arquivo_pikachu = Path('pikachu.json').read_text()
a_json = json.loads(arquivo_pikachu)
print(a_json[1]['ability'])
