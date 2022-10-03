# Polimorfismo
print(10 + 20)
print('Olá' + ' Dev!')

print(len('livro'))
print(len([25,20,30]))
print(len({'Título':'Livro1', 'Lançamento':'2010', 'Categoria':'Lifestyle'}))

###########
class Carro:
    def ligar(self):
        print('Ligando o carro')

class Moto:
    def ligar(self):
        print('Ligando a moto')

def iniciar(veiculo): # Iniciar é polimorfico
    veiculo.ligar()

carro = Carro()
moto = Moto()

iniciar(carro)
iniciar(moto)

###########
class Pessoa:
    def apresentar(self, nome, idade=None, profissao=None):
        if idade and profissao != None:
            print(f'Nome: {nome}: \nIdade: {idade}, \nProfissao: {profissao}')
        elif idade != None:
            print(f'Nome: {nome}, \nIdade: {idade}')
        elif profissao != None:
            print(f'Nome: {nome}, \nIdade: {profissao}')
        else:
            print(f'Nome: {nome}')


print('-'*15)
pessoa = Pessoa()
pessoa.apresentar(nome='Amanda', idade=18, profissao='Programadora')
print()
pessoa.apresentar(nome='Amanda', idade=18)
print()
pessoa.apresentar(nome='Amanda', profissao='Programadora')
print()
pessoa.apresentar(nome='Amanda')