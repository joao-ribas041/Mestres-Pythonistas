from carro import ligar_carro
from moto import ligar_moto

ligar_carro()
ligar_moto()

if __name__ == '__main__':
    print('Ligando veiculos')
    print(f'Estamos no arquivo {__name__}')
