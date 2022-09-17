# Valores aleatórios com random
import random

# Gera um valor de 0.0 a 1.0
print(random.random())

# Gera um valor decimal de Valor Mínimo ao Valor Máximo
print(random.uniform(4, 10))

# Gera um valor inteiro de Valor Mínimo ao Valor Máximo
print(random.randint(4, 10))

cores = ['verde', 'vermelho', 'azul', 'roxo']  # Escolher opção aleatória
print(random.choices(cores, k=3))

cartas_de_um_baralho = ['carta1','carta2','carta3','carta4','carta5',] # Embaralhar uma lista
print(random.shuffle(cartas_de_um_baralho))
print(cartas_de_um_baralho)
print()

# ​# DESAFIO 🥇

# # Desafios Random 

# 1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
# jogue as opções dentro de uma variável e depois crie um programa que 
# imprimir 'cara' ou 'coroa' na tela
moeda = ['cara', 'coroa']
print(random.choice(moeda))
print()

# 2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes
# Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela
lista_de_nomes = ['João', 'Mariana', 'Pedro', 'Tadeu', 'Louiz']
print(random.choice(lista_de_nomes))
print()
# 3. você quer escolher aleatóriamente um número de 10-100
# Imprima na tela um valor aleatório entre 10 e 100
print(random.randint(10, 100))








