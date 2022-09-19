trabalho_terminado = True
if trabalho_terminado == True:
    print('Bora dar uma saida!')
else:
    print('Não posso sair agora')


'''
if condicao:
    # comandos a serem executados
else:
    # condicao oposta
'''

numeros_atrasos = 2
if numeros_atrasos >= 3:
    print('Vá para a diretoria.')
elif numeros_atrasos == 2:
    print('Essa é sua segunda falta')
elif numeros_atrasos == 1:
    print('Essa é sua primeira falta')
else:
    print('Pode entrar')

'''
A velocidade máxima para esssa rua é 50km
* Cruzou entre 51 a 60, levou multa de 2 pontos
* Cruzou entre 61 a 75, levou multa de 3 pontos
* Cruzou acima de 75km, levou multa de 7 pontos
'''
# Chaining

velocidade = 100
if velocidade <= 50:
    print('Não foi multado.')
# elif velocidade >= 51 and velocidade <= 60:
elif 51 <= velocidade <= 60:
    print('Levou multa de 2 pontos')
elif velocidade >= 61 and velocidade <= 75:
    print('Levou multa de 3 pontos')
else:
    print('Levou multa de 7 pontos')

'''
Desafio 🥇

# Monte o seguinte cenário usando condicionais

# Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos grandes que irá seguir as seguinte regras

# Disclaimer the haircut values are completely ficticious, I have no ideia of actual prices

###

Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00

Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00

Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00

Acima de 50cm Favor consultar na recepção

# Declare uma variável que represente o tamanho atual do cabelo

# Apenas imprima na tela a mensagem apropriada, nada além disso é necesário
'''
print()
tamanho_cabelo = 51
if tamanho_cabelo <= 20:
    print('R$50,00 reais o corte.')
elif 21 <= tamanho_cabelo <= 30:
    print('R$70,00 reais o corte.')
elif 31 <= tamanho_cabelo <= 50:
    print('R$100,00 reais o corte.')
else:
    print('Favor consultar a recepção.')
