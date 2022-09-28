try:
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    print(meses[15])
except IndexError as erro:
    print('Favor acessar um índice válido')
    print(erro)

# https://docs.python.org/pt-br/3/library/exceptions.html