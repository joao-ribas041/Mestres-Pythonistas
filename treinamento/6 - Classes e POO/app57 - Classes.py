""" # Código solto
marca = input('Digite a marca do seu computador: ')
memoria = input('Digite a quantidade de memória ram: ')
placa = input('Digite o nome da placa de vídeo: ')

print(f'Seu computador é da marca: {marca}')
print(f'Seu computador possui {memoria} de memória')
print(f'Seu computador possui uma placa de vídeo: {placa}')


# Funções
def exibir_informacoes_do_computador():
    marca = input('Digite a marca do seu computador: ')
    memoria = input('Digite a quantidade de memória ram: ')
    placa = input('Digite o nome da placa de vídeo: ')

    print(f'Seu computador é da marca: {marca}')
    print(f'Seu computador possui {memoria} de memória')
    print(f'Seu computador possui uma placa de vídeo: {placa}')

exibir_informacoes_do_computador()
 """

# Classes
class Computador:
    def __init__(self, marca, memoria_ram,placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

computador1 = Computador('Asus','16gb','Nvidia')
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_video)

computador2 = Computador('Avell','32gb','1660ti')
print(computador2.marca)
print(computador2.memoria_ram)
print(computador2.placa_de_video)
