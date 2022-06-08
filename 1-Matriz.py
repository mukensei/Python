#Actividad 3 - Ejercicio 1 Operaciones con Matrices

import copy
class Matriz():
  def __init__(self, matriz):
    self.matriz = matriz
    pass

  def __add__(self, other):
    self.matriz = other
    matriz1 = self.matriz
    matriz1 = ([1,2,3],[4,5,6])
    print("A la matriz:", matriz1)
    matriz_resultado=([0,0,0], [0,0,0])
    n_filas = len(matriz_resultado)
    n_columnas = len(matriz_resultado[0])
    matriz2 = copy.deepcopy(matriz1)
    print("Se le sumará:", matriz2)
    for i in range (n_filas):
      for j in range (n_columnas):
        matriz_resultado[i][j]=(matriz1[i][j]+matriz2[i][j])
    return matriz_resultado

  def __sub__(self, other):
    self.matriz = other
    matriz1 = self.matriz
    matriz1 = ([1,2,3],[4,5,6])
    print("A la matriz:", matriz1)
    matriz_resultado=([0,0,0], [0,0,0])
    n_filas = len(matriz_resultado)
    n_columnas = len(matriz_resultado[0])
    matriz2 = copy.deepcopy(matriz1)
    print("Se le restará:", matriz2)
    for i in range (n_filas):
      for j in range (n_columnas):
        matriz_resultado[i][j]=(matriz1[i][j]-matriz2[i][j])
    return matriz_resultado
    
  def __mul__(self, other):
    self.matriz = other
    matriz1 = self.matriz
    matriz1 = ([1,2,3],[4,5,6])
    print("La matriz:", matriz1)
    matriz_resultado=([0,0,0], [0,0,0])
    n_filas = len(matriz_resultado)
    n_columnas = len(matriz_resultado[0])
    matriz2 = copy.deepcopy(matriz1)
    print("Se multiplicará por:", matriz2)
    for i in range (n_filas):
      for j in range (n_columnas):
        matriz_resultado[i][j]=(matriz1[i][j]*matriz2[i][j])
    return matriz_resultado

  def mostrar(self, matriz):
    print("Resultado:", str(matriz_resultado))
    
  def __str__(self):
    return '[[1,2,3],[4,5,6]]'.format(matriz)

print("SUMA\n")      
matriz = Matriz([[1,2,3],[4,5,6]])
matriz_resultado = matriz + matriz
print(str(matriz_resultado))
print("\nRESTA\n")
matriz_resultado = matriz - matriz
print(str(matriz_resultado))
print("\nMULTIPLICACIÓN\n")
matriz_resultado = matriz * matriz
print(str(matriz_resultado))
