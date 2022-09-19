# Loops Aninhados
# Pais + Estação

paises = ['Brasil', 'India', 'Estados Unidos']
estacoes_do_ano = ['Primavera', 'Verão', 'Outono', 'Inverno']
for pais in paises:
    for estacao in estacoes_do_ano:
        print(f'{pais} {estacao}')
    print()

for x in range(1, 11):
    for y in range(1, 6):
        print(f'Valor externo {x} e interno de {y}')
print()

# Desafio
# Imprima na tela a marca + celular de todos os celulares, usando as informaçoes abaixo

celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'{celular} {versao}')
    print()
