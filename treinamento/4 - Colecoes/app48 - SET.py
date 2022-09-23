'''
# SET
numeros = [2, 2, 5, 8]
frutas = {'Maça', 'Uva', 'Banana', 'Maça', 'Morango'}

# Convertendo para set
set_numeros = set(numeros)
set_frutas = set(frutas)

print(set_numeros)
print(set_frutas)

# Adicionando novos valores
set_numeros.add(10)
print(set_numeros)
'''
# Conjuntos
numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]
a = set(numeros1)
b = set(numeros2)

print(numeros1)
print(a)
print()
print(numeros2)
print(b)
print()
print(a.symmetric_difference(b))  # valores unicos
print(a.intersection(b))  # valores em comum
