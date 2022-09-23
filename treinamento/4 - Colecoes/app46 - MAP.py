# Como podemos criar listas?

# Criar listas usando Loops e Range()

numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# Map
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']


def aprovar_pessoa(nome):
    # Logica mais complexa
    return nome + ' APROVADO'


print(list(map(aprovar_pessoa, nomes)))

print()
# DESAFIO -
# ExtraiA as cores da lista a seguir e coloque as em uma
# nova lista. Finalmente imprima a nova lista na tela.
pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]
print(pinturas)
cores = []

for pintura in pinturas:
    print(pintura)
    cores.append(pintura[1])

print(f'Cores: {cores}')
