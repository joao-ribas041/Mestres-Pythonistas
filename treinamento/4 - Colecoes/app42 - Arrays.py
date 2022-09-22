# Arrays
# https://docs.python.org/pt-br/3.7/library/array.html
from array import array
# Inteiros, números decimais e caracteres
numeros = array('i', [1, 2, 3, 4, 5, 6])
print(numeros)
numeros.append(10)
print(numeros)
numeros.insert(5, 200)
print(numeros)
numeros.pop(1)
print(numeros)
numeros.remove(5)
print(numeros)
del numeros[1]
print(numeros)
