'''
from datetime import datetime


def comprar_equipamentos():
    return 'Estou comprando equipamentos'


def depositar_dinheiro():
    print('Depositando dinheiro')

    def depositando_dolar():
        print('Depositando dolares')

    def depositando_reais():
        print('Depositando reais')

    depositando_dolar()
    depositando_reais()


depositar_dinheiro()


def pai(numero):
    def filho_1():
        print('Sou filho 1')

    def filho_2():
        print('Sou filho 2')

    if numero == 1:
        return filho_1


resultado = pai(1)
resultado()

#########
# Decorators
#####

def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper


@meu_decorator
def parabenizar():
    print('Parabéns!!!!')


resultado = meu_decorator(parabenizar)
resultado()
'''

# DESAFIO 1
# Crie um decorador que irá pegar a função que for passado para ele e imprimir
# o horário atual antes de executar a função e depois imprimir o horário após
# ter finalizado a execução da função.

# * Dica: você terá que usar o módulo datetime para conseguir o horário atual

from datetime import datetime


def meu_decorator(funcao):
    def wrapper():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return wrapper


@meu_decorator
def teste_horario():
    print('Parabéns, você resgatou as horas')


teste_horario()
