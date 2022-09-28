"""
COMO CRIAR E MODIFICAR ARQUIVOS:
'w'  -> Usado somente para escrever algo
'a'  -> Usado para acrescentar algo
'r'  -> Usado somente para ler algo
'r+' -> Usado para ler e escrever algo
"""
import os

# with open('celulares.txt','w') as arquivo:
#     arquivo.write('Celular 2')

nomes = ['João','Mariana','Rafael','Felipe','Renato']
numeros = [1,2,3,4,5,6]
"""
with open('nomes.txt','a', newline='') as arquivo:
    for nome in nomes:
        arquivo.write(nome + os.linesep)
"""

# with open('numeros.txt', 'a', newline='') as arquivo:
#     for numero in numeros:
#         arquivo.write(str(numero) + os.linesep)


# with open('nomes.txt', 'r') as arquivo:
#     for linha in arquivo:
#         print(linha)
""" 
with open('numeros.txt','r+') as arquivo:
    for linha in arquivo:
        print(linha)
        num = int(linha)
        print(f'\nEscrita: {num}')
    arquivo.write(str(num + 1))  """


# 🥇 DESAFIO Manipulação de Arquivos🥇
'''
Veja o desafio, tente fazer por conta própria e depois veja a solução que estou passando aqui

# Primeiro crie 3 listas
 * Uma lista que contem 5 frutas
 * Uma lista que contem 5 cores
 * Uma lista que contem 5 linguagens de programação
'''
import os
frutas = ['Banana', 'Maça', 'Abacate', 'Morango', 'Uva']
cores = ['Vermelho', 'Azul', 'Preto', 'Verde', 'Amarelo']
linguagens = ['Python', 'Java', 'C Sharp', 'JavaScript', 'React Native']



# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
print('-1-'*10)
print('Criando arquivo...')
with open('frutas.txt','w', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
print('-2-'*10)
print('Lendo arquivo...')
with open('frutas.txt','r') as arquivo:
    for linha in arquivo:
        print(linha)

# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
print('-3-'*10)
with open('frutas.txt','a', newline='') as arquivo:
    for cor in cores:
        arquivo.write(os.linesep + cor)

# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.
print('-4-'*10)
with open('Top 5 linguagens.txt','w', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)

# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?
print('-BONUS-'*3)
for i in range(1,6):
    with open('Arquivo' + str(i) +'.txt','w') as arquivo:
        arquivo.write(f'Arquivo {i}')



