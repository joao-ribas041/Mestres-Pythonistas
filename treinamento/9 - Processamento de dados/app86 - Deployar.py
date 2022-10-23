import time

cont = 0
while True:
    print('estamos funcionando :)')
    time.sleep(3)
    cont += 1
    if cont >=10:
        print('Encerrando')
        break
print('finalizado')
