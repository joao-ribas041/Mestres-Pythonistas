teclado = 'Teclado'
print(teclado[-1])
print(teclado.index('l'))
print(teclado[teclado.index('l')])
# Acessando partes de um string
link = 'facebook.com/devaprender'
print(link[0])
print(link[-1])
print(link[0:5])
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5])

frase = 'Clean Code'
print(frase.rindex('C'))
print()
# DESAFIO 1 🥇

# Desafio 1 Encontre o índice de 'o' dentro da variável biblioteca

biblioteca = 'Biblioteca'
print(frase.index('o'))

# Desafio 2

# Usando a frase

frase = 'Desenvolvimento De Aplicações'

# Imprima apenas 'De Aplicações'
indice_d = frase.rindex('D')
indice_s = frase.rindex('s')
print(frase[indice_d:indice_s+1])
