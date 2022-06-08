def fibonacci_iterativo(n):
  f = [0,1]
  g = [1]
  if n==0:
    return [0]
  else:
    for i in range (2,n+1):
      f.append(f[i-1] + f[i-2])
      g.append(f[i-1] + f[i-2])
  return g


def fibonacci_recursivo(x):
    if x < 2:
        return x
    else:
        fibo = fibonacci_recursivo(x - 1) + fibonacci_recursivo(x - 2)
        return fibo

x=int(input("Ingerse el número de términos que desea: "))

print("Resultado Iterativo", fibonacci_iterativo(x))
print("Resultado Recursivo", fibonacci_recursivo(x))
