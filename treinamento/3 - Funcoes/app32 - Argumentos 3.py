# Kwargs - Funções com nº de argumentos nomeados dinamicos
# **kwargs(keyword arguments)

def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)


concatenar(a='Nós', b='Somos', c='Pythonistas', d='Profissionais')


def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)


fazer_calculo('Jeff', 4, 6, 3, 7, a=1, b=2, c=3)
