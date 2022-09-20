'''
# Funções
def nome_da_funcao(parametros):
    comandos
'''


def dar_boas_vindas():
    print('Bem-Vindo!')


def dar_boas_vindas_personalizada(nome):
    print(f'Bem-vindo(a) {nome}')


dar_boas_vindas()
dar_boas_vindas_personalizada(input('Digite seu nome: '))


# Valor padrão
def apresentar_lugar(horario_de_funcionamento, lugar='nossa loja'):
    print(
        f'Conheça {lugar}, horario de funcionamento das {horario_de_funcionamento}.')


apresentar_lugar('08:00 as 18:00', 'Disney')
print()

# Desafio🥇
# DESAFIO 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa


def gerar_nome_completo(nome, sobrenome):
    print(f'Bem vindo(a) {nome} {sobrenome}.')


gerar_nome_completo('João', 'Ribas')
print()

# DESAFIO 2 - # Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preco de um produto e o segundo parâmetro é a quantidade, porém a quantidade deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.


def calcular_valores(preco, quantidade=1):
    print(f'Valor: {preco}, Quantidade: {quantidade}')
    print(f'Valor total: {preco * quantidade}')


calcular_valores(10, 20)
