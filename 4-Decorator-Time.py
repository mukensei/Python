#Crea un decorator @get_time que cuando se añada a una función imprima por pantalla:
# 1. El tiempo cuando ha empezado la función
# 2. El tiempo cuando ha acabado la función
# 3. El tiempo total ...Ejemplo con función “dormir_2s”:...

from datetime import datetime
import time

def get_time(func):
    def wrapper():
        print(f'{"."*40}')
        print(f'Nombre de la función: {func.__name__}\nHora de inicio: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        v=datetime.now()
        print(f'{"_"*40}')
        func()
        print(f'Finaliza la función: {func.__name__}\nHora de finalización: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"_"*40}')
        w=datetime.now()
        print("\nTiempo Empleado por la función\n(H. Fin - H. Inicio)\n",w-v)
        print(f'{"_"*40}')
        
    return wrapper

@get_time
def dormir_2s():
    print('\nMe he quedado dormido...\n')
    time.sleep(2)
    print('Me he despertado\nListo para volver a programar. ^_^\n')      

dormir_2s()

