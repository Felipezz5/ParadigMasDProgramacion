import time
from memory_profiler import memory_usage

def facto_r(n):
    if n == 0 or n == 1:
        return 1
    return n * facto_r(n - 1)

def facto_i(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def medir_tiempos(n):
    start = time.time()
    facto_r(n)
    tiempo_r = time.time() - start

    start = time.time()
    facto_i(n)
    tiempo_i = time.time() - start

    print(f"Socio el tiempo recursivo para tan {n}!: {tiempo_r:.10f} segundos")
    print(f"Socio el tiempo iterativo para tin {n}!: {tiempo_i:.10f} segundos")

def medir_memoria(n):
    memoria_r = memory_usage((facto_r, (n,)), max_iterations=1)
    memoria_i = memory_usage((facto_i, (n,)), max_iterations=1)

    print(f"El uso de memoria recursivo para tan{n}!: {max(memoria_r) - min(memoria_r):.10f} MiB")
    print(f"El uso de memoria iterativo para tin{n}!: {max(memoria_i) - min(memoria_i):.10f} MiB")

if __name__ == "__main__":
    n = 10
    medir_tiempos(n)
    medir_memoria(n)
