import random
import time
from concurrent.futures import ProcessPoolExecutor

def contar_pontos_circulo(num_pontos):
    dentro_circulo = 0
    for _ in range (num_pontos):
        x = random.random()
        y = random.random()
        if x*x + y*y <=1 :
            dentro_circulo += 1
    return dentro_circulo

if __name__ == "__main__":
    total_pontos = 10_000_000
    n_processos = 4
    pontos_por_processo = total_pontos // n_processos

    inicio = time.time()
    with ProcessPoolExecutor(max_workers=n_processos) as executor:
        resultados = list(executor.map(contar_pontos_circulo, [pontos_por_processo]*n_processos))
    dentro_circulo_total = sum(resultados)

    pi = 4 * dentro_circulo_total / total_pontos
    fim = time.time()

    print(f"π ≈ {pi}")
    print(f"Tempo paralelo: {fim - inicio:.2f} segundos")