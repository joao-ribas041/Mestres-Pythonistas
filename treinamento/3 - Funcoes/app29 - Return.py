# Processar vs Retornar
# Funções que apenas processa dados
print('Olá!')

# Funções que retorna dados
cidade = input('Qual é a sua cidade? ')

# Como escolher entre funções que processam VS retornam dados?
''' Eu vou precisar usar essa informação na lógica do meu programa ainda? ou só
preciso processar esse dado? mas não irei utilizar mais ele depois? '''


def exibir_cotacao_do_dia(moeda):
    if moeda == 'usd':
        print(5.47)
        print()


exibir_cotacao_do_dia('usd')


def exibir_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.47


cotacao = exibir_cotacao_do_dia('usd')
print(cotacao)
if cotacao > 5:
    print('Investir em ações americanas')
else:
    print('Cotação não favorável')
