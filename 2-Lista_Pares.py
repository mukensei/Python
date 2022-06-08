#Crea tu propia estructura de datos heredando de la lista de la librería estándar, 
#y añadiendo la funcionalidad que la lista disponga de un atributo 
# n_pares con el número actual de números pares. 
# Esté atributo, tiene que estar siempre actualizado y no debe ser calculado en el momento de su consulta.

class ListaPares():
    def __init__(self, dato):
        self.lista = dato
        self.n_pares = []
        self.contador = 0
        pass
     
    def ingresar_dato(self, dato):
        if dato % 2 == 0:
          self.contador+=1
          self.n_pares.append(dato)
        else:
          self.lista.append(dato)
        return self.lista      
print("Bienvenido, vamos a Ingresar un dato en mi_lista, \nluego veremos si va a la lista de impares o pares.")
mi_lista = ListaPares([])
y = 0
while y<=10:
  x=int(input("Ingresa un Número:"))
  mi_lista.ingresar_dato(x)
  print("Lista: {}, \nPares:, {}, \nContador de Pares ingresados:\n ({}) Pares".format(mi_lista.lista,mi_lista.n_pares, mi_lista.contador))
  y+=1