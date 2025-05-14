import multiprocessing

# Función que calcula el cuadrado de un número
def calcular_cuadrado(n):
    return n * n

# Bloque principal del código
if __name__ == "__main__":
    # Lista de números para calcular sus cuadrados
    numeros = [1, 2, 3, 4, 5]
    
    # Crear un pool de procesos (en este caso con 2 procesos)
    with multiprocessing.Pool(processes=2) as pool:
        # Distribuir el trabajo entre los procesos
        resultados = pool.map(calcular_cuadrado, numeros)
    
    # Imprimir los resultados
    print(resultados)
