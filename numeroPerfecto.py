import time
def es_numero_perfecto(n):
    if n <= 1:
        return False
   
    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n
inicio = time.time()
numero = int(input("Introduce un número: "))
if es_numero_perfecto(numero):
    print(f"{numero} El número es perfecto.")
else:
    print(f"{numero} No es un número perfecto.")
fin = time.time()
tiempo_transcurrido = (fin - inicio) * 1000
print(f"Tiempo de ejecución: {tiempo_transcurrido:.2f} en milisegundos")


