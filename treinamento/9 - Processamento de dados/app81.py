# # # Como podemos criar listas?
# # # Criar listas usando Loops e Range()
# # numeros = []
# # for i in range(5):
# #     numeros.append(i)
# # print(numeros)

# # # Map
# # nomes = ['Larissa','Rafael','Marcus','John']
def aprovar_pessoa(nome):
    # Lógica mais complexa
    return nome + ' Aprovado'
    
# # print(list(map(aprovar_pessoa,nomes)))

# # Como usar uma list compreheension
# nova_lista = [2 * i for i in range(10)]
# # [expressao for membro in iterável]
# print(nova_lista)

# nomes = ['Larissa','Rafael','Marcus','John']
# print([nome + ' APROVADO' for nome in nomes])
# print([aprovar_pessoa(nome) for nome in nomes])

""" 1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5 """

from pprint import pprint
pprint([[i for i in range(1, 6)] for x in range(5)])
# Usar condicionais em list compreeheension
# [expressao for membro in iterável(condicional if)]
nomes = ['Larissa','Rafael','Marcus','John']
print([aprovar_pessoa(nome) for nome in nomes if nome != 'Rafael'])

# Valores numéricos
def eh_numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False

print([i for i in range(20) if eh_numero_par(i)])

# A condicional é flexível
# [expressao (condicional if) for membro in iterável]
participantes = ['Larissa', 'Rafael', 'Marcus', 'John']
ganhadores = ['Marcus', 'John']
print([i + ' GANHADOR' if i in ganhadores else i + ' NÃO SELECIONADO' for i in participantes])



print('-'*15)
# # DESAFIO 1
# Usando a list compreheension, crie a seguinte lista:
# [2, 4, 6, 8, 10] 

print([i * 2 for i in range(1, 6)])



# # DESAFIO 2
# Use a lista compreheension usando a seguinte lista como base:
# cores = ['vermelho','azul','verde','amarelo','rosa','preto'] 

# para criar a lista seguir
# ['1 - vermelho','2 - azul','3 - verde','4 - amarelo','5 - rosa','6 - preto'] 
cores = ['vermelho','azul','verde','amarelo','rosa','preto'] 
pprint([str(cores.index(cor)+1) + ' - ' + cor for cor in cores])


# # Desafio 3
# Usando a lista seguir como base:
# participantes = ['joel','jessica','maria','cris','larissa','rafael','marcus','john']
# pagamento_realizado = ['joel','jessica','maria','cris']
# concatene(adicione) a palavra ' PAGO' aos nomes da lista 'participantes' usando condicionais,
# somente nos casos onde seu nome esteja na lista 'pagamento_realizado', o resultado final deve ter como a lista a seguir:
# []

participantes = ['joel','jessica','maria','cris','larissa','rafael','marcus','john']
pagamento_realizado = ['joel','jessica','maria','cris']

print([participante + ' PAGO' for participante in participantes])
pprint([i + ' PAGO' if i in pagamento_realizado else i + ' DEVENDO' for i in participantes])


