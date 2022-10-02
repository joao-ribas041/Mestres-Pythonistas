# Métodos Mágicos(Magic Methods, dunder methods(double underscore))
class Pessoa:
    def __init__(self):
        self.nome = 'Sou uma pessoa'
        self.habilidades = ['Habilidade 1', 'Habilidade 2', 'Habilidade 3']
    
    def __repr__(self):
        return 'Classe pessoa com propriedades nome e habilidades'

    # O que deve ser mensurado para determinar o quantidade daquela classe(chamada com método(len(pessoa)))
    def __len__(self):
        # len(pessoa) ?
        return len(self.habilidades)

    def __str__(self):
        return f'{self.nome} com as habilidades {self.habilidades}'


pessoa = Pessoa()
print(pessoa.nome)
print(repr(pessoa))
print(len(pessoa))
print(pessoa)
print(dir(pessoa))
