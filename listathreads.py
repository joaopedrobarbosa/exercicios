# --- Importando módulos
import threading
import time

lista = []
def produtor():
    global lista
    falhas = 0
    for i in range(100):
        if(len(lista) < 50):
            lista.append('informação')
            print('produziu')
            time.sleep(2)
        else:
            falhas += 1
    
    print(f'ocorreu {falhas} erros ao produzir')
    

def consumidor():
    global lista
    falhas = 0
    for i in range(100):
        if(len(lista) > 0):
            lista.pop()
            print('consumiu')
        else:
            falhas += 1

    print(f'ocorreu {falhas} erros ao consumir')
        

produtora = threading.Thread(target=produtor, args=( ))
consumidora = threading.Thread(target=consumidor, args=())

produtora.start()
consumidora.start()

produtora.join()
consumidora.join()
print(len(lista))
