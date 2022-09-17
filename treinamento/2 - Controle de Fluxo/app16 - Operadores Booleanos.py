# Vamos pensr por exemplo no seguinte:
idade = 21
possui_convite = True
filho_do_dono = True

print((idade >= 21) and (possui_convite == True))  # e &
print(idade >= 21 or possui_convite == True)  # ou

# maior de 21 e possui convite ou seja filho do dono
# print((idade > 21 and possui_convite == True) or (filho_do_dono == True))
print(idade > 21 and possui_convite == True or filho_do_dono == True)


maior_de_idade = True
possui_carteira_de_trabalho = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False
print('\nVocê só pode trabalharv aqui se for maior de idade e possuir carteira de trabalho')
print(maior_de_idade == True and possui_carteira_de_trabalho == True)
# mesma coisa que (True and True)
print(maior_de_idade and possui_carteira_de_trabalho)

print('\nQueremos contratar pessoas que ainda não possuem um veículo próprio, mas já possuam uma carteira de trabalho.')
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio)

# precedência de Operadores
"""
Operadores          -   Significados
.().                -   Parenteses
**                  -   Expoente
*                   -   Multiplicação
/                   -   Diivisão
//                  -   Divisão por inteiros
%                   -   Modulos
+,-                 -   Adição, Subtração

==,!=,>,<,>=,<=,
is not, in, not in  - Comparadores lógicos, identidade, pertencimento conjuntos  

not         -   NOT booleano
and         -   AND booleano
or          -   OR booleano
"""

print()
print('-'*15)
# Quero que você defina as seguintes variáveis, inicialmente todas como False, a ideia aqui não é de se importar com os valores dentro dessas variáveis, mas sim como montar condicionais.
possui_passaporte = True
passagem_comprada = True
menor_de_idade = False
# E Crie as seguintes condições usando o que acabou de ver e imprima o resultado na tela. Tente fazer cada condição e depois veja a solução no final deste aula.

print('\nUma pessoa só pode viajar se possuir passaporte e tiver a passagem comprada e não for menor de idade')
print((possui_passaporte and passagem_comprada) and not menor_de_idade)

print('\nUma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade')
print((possui_passaporte or passagem_comprada) and not menor_de_idade)

print('\nUma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade')
print((not possui_passaporte or passagem_comprada) and not menor_de_idade)

print('\nUma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade')
print((not possui_passaporte or not passagem_comprada) and menor_de_idade)

print((possui_passaporte or not passagem_comprada) and not menor_de_idade)
