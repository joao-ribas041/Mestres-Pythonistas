import webbrowser
import threading
import time

def comentar(site):
    if site == 8:
        raise Exception(f'OUVE UM ERRO GRAVE {site}')
    print(f'Entrando no site: {site}')
    time.sleep(5)
    print(f'Dados processados no site: {site}')
    
threads = []
for site in range(100):
    nova_thread = threading.Thread(target=comentar, args=(site,))
    threads.append(nova_thread)
    
for thread in threads:
    thread.start()
    print(f'Iniciando {thread.name}')
    
for thread in threads:
    thread.join()
    print(f'Finalizadno {thread.name}')