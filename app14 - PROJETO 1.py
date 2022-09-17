from datetime import datetime
import random

nome = str(input('Digite o seu nome: '))
idade = int(input('Digite sua idade: '))
data_cadastro = datetime.strftime(datetime.now(), '%d/%m/%Y')
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
cartao_usuario = random.choice(cartoes)
data_aniversario = datetime.strptime(
    input('Digite o dia do seu aniversario: '), '%d/%m/%Y')


def apresentar_usuario():
    print(
        f'\nOlá {nome}, seu registro foi concluído com sucesso no dia {data_cadastro}.')
    print(
        f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao_usuario}.')


# cadastro_usuario()
apresentar_usuario()
