import webbrowser
import threading
import time
""" def comentar(site, comentario):
    print(f'Entrando no site: {site}')
    print(f'Deixando um comentario: {comentario}')
    time.sleep(5)
    print(f'Dados processados no site: {site}')
    
comentarios = ['oi', 'ola', 'gostei', 'curti', 'muito bom']
threads = []
for site in range(6):
    nova_thread = threading.Thread(target=comentar, args=(site, random.choice(comentarios)))
    threads.append(nova_thread)
    
for thread in threads:
    thread.start()
    print(f'Iniciando {thread.name}')
    
for thread in threads:
    thread.join()
    print(f'Finalizadno {thread.name}') """
    
    
# Desafio 2
print('\n'*4)
import random

def extrair_produtos(site, produto):
    print(f'\nNavegando ate {site}')
    # time.sleep(2)
    print(f'Extraindo produto: {produto}')
    
site = 'www.mercadolivre.com'
produtos = ['celular','monitor','fone de ouvido', 'auto-falante','computador']
threads = []

for i in range(1,6):
    threads.append(threading.Thread(target=extrair_produtos,args=(site, random.choice(produtos)),daemon=True))

for thread in threads:
    thread.start()
    time.sleep(1)
    
for thread in threads:
    thread.join()
    

