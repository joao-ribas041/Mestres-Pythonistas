from turtle import Turtle

# Inicializar uma turtle
t = Turtle()

# Definir a velocidade:
t.speed(1)


while True:
    contunua = str(input('Deseja continuar? [s/n] '))
    if contunua == 'n':
        break
    else:
        distancia = int(input('Digite uma distancia: '))
        t.forward(distancia)

print('Finalizado')
'''
# Movimentar a turtle para frente
t.forward(100)

# Rotacionar a turtle em x graus para a direita.
t.right(90)
t.forward(100)

# Rotacionar a turtle em x graus para a esquerda.
t.left(90)
t.forward(100)

# Movimentar a turtle para trás
t.backward(200)
input()
'''
