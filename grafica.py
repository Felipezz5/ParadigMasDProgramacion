import time
import matplotlib.pyplot as plt

def facto_r(n):
    if n == 0 or n == 1:
        return 1
    return n * facto_r(n - 1)

def facto_i(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

n_values = list(range(1, 100))
tiempos_r = []
tiempos_i = []

for n in n_values:
    start = time.time()
    facto_r(n)
    tiempos_r.append(time.time() - start)

    start = time.time()
    facto_i(n)
    tiempos_i.append(time.time() - start)

plt.plot(n_values, tiempos_r, label="Recursivo")
plt.plot(n_values, tiempos_i, label="Iterativo")
plt.xlabel("n")
plt.ylabel("Tiempo")
plt.title("Comparación: Recursivo vs Iterativo")
plt.legend()
plt.grid(True)
plt.savefig("comparacion_tiempos.png")
plt.show()
