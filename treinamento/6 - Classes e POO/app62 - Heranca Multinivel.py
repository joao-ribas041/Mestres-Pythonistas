# Herança multinível
class Usuario:
    def __init__(self,nome,salario,profissao):
        self.nome = nome
        self.salario = salario
        self.profissao = profissao

    def registrar_funcionario(self):
        print(f'Cadastrando o usuário {self.nome}')

class Gestor(Usuario):
    def __init__(self,nome,salario,profissao,setor_responsavel):
        super().__init__(nome.salario.profissao)
        self.setor_responsavel = setor_responsavel

    def definir_setor(self, setor):
        print(f'Definindo setor para {setor}')

usuario1 = Usuario('Camila', 5000, 'Analista de Software')
gestor = Gestor('Roberta', 7000, 'Gestora', 'Gestão de Projetos')

# Herança multinível
# 1º problema
class Veiculo:
    pass

class VeiculoDeRoda(Veiculo):
    quantidade_maxima_de_rodas = 2
    pass

class Carro(VeiculoDeRoda):
    pass

class CarroEletrico(Carro):
    pass

class CarroEletricoDuasPortas(CarroEletrico):
    pass
