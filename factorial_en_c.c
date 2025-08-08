#include <stdio.h>
#include <time.h>

int facto_r(int n) {
    if (n == 0 || n == 1)
        return 1;
    return n * facto_r(n - 1);
}

int facto_i(int n) {
    int resultado = 1;
    for (int i = 2; i <= n; i++)
        resultado *= i;
    return resultado;
}

int main() {
    int n = 10;
    clock_t start, end;
    double tiempo;

    start = clock();
    facto_r(n);
    end = clock();
    tiempo = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Socio el tiempo recursivo para tin %d!: %f segundos\n", n, tiempo);

    start = clock();
    facto_i(n);
    end = clock();
    tiempo = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Socio el tiempo iterativo para tan %d!: %f segundos\n", n, tiempo);

    return 0;
}
