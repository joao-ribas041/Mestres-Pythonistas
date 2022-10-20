import webbrowser
import threading
import time
import random

def comentar(site, comentario):
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
    print(f'Finalizadno {thread.name}')
    