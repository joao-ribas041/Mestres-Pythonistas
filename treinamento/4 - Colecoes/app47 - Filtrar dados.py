# Filtrar
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']


def pessoa_aprovada(pessoa):
    if pessoa == 'Marcus':
        return True
    else:
        return False


print(list(filter(pessoa_aprovada, nomes)))
print(list(map(pessoa_aprovada, nomes)))

# Filter
pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]


def eh_antiguidade(pintura):
    print(pintura)
    if pintura[2] < 1890:
        return True
    else:
        return False


print(list(filter(eh_antiguidade, pinturas)))
print()

# DESAFIO 1 🥇
'''
Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500
'''
vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]


def salario_bom(vaga):
    if vaga[1] > 2500:
        return True
    else:
        return False


print(list(filter(salario_bom, vagas)))
