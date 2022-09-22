# Enumerate
for indice, numero in enumerate(range(1, 11), 1):
    print(indice, numero)
    if indice == 5:
        print('Estamos na metade da lista')
print()
nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']

for nome in enumerate(nomes, 1):
    print(indice, nome)
    if indice == 3:
        print('Já temos 3 pessoas registradas')

# Desafio1
# Itere sobre a lista abaixo exibindo o número
# do índice + nome da fruta. Porém quando o
# índice for 3 exiba 'N°' índice + nome da fruta EM PROMOÇÃO

frutas = ['Maça', 'Laranja', 'Morango', 'Limão']

for indice, fruta in enumerate(frutas, 0):
    if indice == 3:
        print(f'{indice}, {fruta} EM PROMOÇÃO')
    else:
        print(f'{indice} {fruta}.')
