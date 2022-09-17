from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data
lancamento_app = datetime(2022, 10, 10)
print(lancamento_app)
# Quero receber a data de lançamento do meu aplicativo
data_de_lancamento = datetime.strptime(
    input('Quando devemos lançar o aplicativo? '), '%d/%m/%Y')
print(type(data_de_lancamento))

data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)

# DESAFIO 🥇

# Calcule quantos dias faltam até o seu aniversário
data_de_lancamento = datetime.strptime(
    input('Qual é o dia do seu aniversario? '), '%d/%m/%Y')
prazo = data_de_lancamento - data_atual
print(f'Faltam {prazo} dias para o seu aniversario.')
print(type(prazo))
