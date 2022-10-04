# Refatoração
# Renomear todas ocorrências - F2


class calc:
    pass

calc1 = calc()
calc2 = calc()
calc3 = calc()

print(calc1)
# Extrair função(CTRL-SHIFT-P Extract Method - Atalho: em)
def adicao():
    resultado = 20 + 50
    
adicao()

# Extrair função(CTRL-SHIFT-P Extract Variable - Atalho: ev)
altura = 60
largura = 2
tamanho = (altura/largura) + 50
