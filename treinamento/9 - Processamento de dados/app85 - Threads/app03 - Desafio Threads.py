import webbrowser
import threading
import time

def navegar(site):
    print(f'Navegando até o site {site}')
    time.sleep(2)
    webbrowser.open_new(site)
    for i in range(6):
        print(f'Carregando {i}/5')
        time.sleep(1)
    print(f'\nSite carregado.')
    
def baixar_fotos(site):
    print(f'Iniciando download de fotos do site {site}')
    for i in range(11):
        print(f'Baixando fotos {i}/10')
        time.sleep(1)
    print('\nFotos baixadas com sucesso.')
    
    
url = 'http:www.google.com'
nova_thread = threading.Thread(target=baixar_fotos, args=(url,),daemon=True)
nova_thread.start()
navegar(url)
nova_thread.join()
