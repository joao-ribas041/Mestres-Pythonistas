'''
# continue, ignorar/pular
for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        continue
print()
# break, para interromper a iteração
for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        break
print()
frutas = ['Maça', 'Manga', 'Laranja', 'Morango']
for fruta in frutas:
    if fruta == 'Manga':
        continue
    print(f'{fruta} adicionada a dieta')
'''

# DESAFIOS 🥇
# Desafio 1
# Use a operação necessária(break ou continue) para que a seguinte condição aconteça.
# Ao cegar ao estilo "Rap" o mesmo não deve ser impresso na tela
estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(f'{estilo}')
print()
# Desafio 2
# Use a operação necessária(braek ou continue) para que a seguinte condição aconteça:
# Ao chegar ao estilo "Rock" a execução deve interrompida
estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rock':
        break
    print(f'{estilo}')
print('Finalizado.')
