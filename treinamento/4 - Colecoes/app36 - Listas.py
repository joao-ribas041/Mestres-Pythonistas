'''
preco_1 = 10
preco_2 = 20
preco_3 = 30

# listas
precos = [10, 20, 30, 40, 50, 60, 100, 250, 230, 560, 23, 74]
#         0   1   2
print(precos[0])  # Indice
print(precos[precos.index(100)])

# listas no python são dinâmicas(aceitam qualquer tipo de dado)
itens = [1, 2, 3, 'Olá', 'Café', True, 10.6]
print(itens[4])

# Maneiras diferentes de gerar uma lista
# Multiplicação de valores(repetição)
lista_de_noves = [9] * 10
lista_de_noves = ['Teste'] * 10
print(lista_de_noves)

# Usando gerador Range(Sequência)
# 1 até 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)

# Gerar apartir de strings
print(list('Bem-vindo ao treinamento'))

# Lista de uma lista(matriz)
matriz_de_nomes = [['Carol', 30], ['Marcus', 50]]
print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0])
print(matriz_de_nomes[1][0])
'''
# Desafios 🥇
# Desafio #1 Crie uma lista que tenha os nomes dos 3 objetos que você mais
# usa durante o dia e imprima ele na tela
objetos = ['Celular', 'Notebook', 'Moto']
print(objetos)
print()

# Desafio  # 2 Usando apenas uma linha de código, crie uma lista de 10 a 131
lista_de_10_a_132 = list(range(10, 132))
print(lista_de_10_a_132)
print()

# Desafio  # 3 Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2
print(objetos, lista_de_10_a_132)

# Desafio  # 4 Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos
# que você mais usa durante o dia, mas agora dentro de cada item você vai colocar
# uma informação extra, coloque o valor em reais desse objeto também e imprima ele na tela
matriz_objetos = [['Celular', 2000], ['Notebook', 8000], ['Moto', 30000]]
print(matriz_objetos[1][0])
