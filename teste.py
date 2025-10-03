import random
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool

def contar_pontos_circulo(num_pontos):
    dentro_circulo = 0
    for _ in range (num_pontos):
        x = random.random()
        y = random.random()
        if x*x + y*y <=1 :
            dentro_circulo += 1
    return dentro_circulo

if __name__ == "__main__":
    # ================================
    # PARALELO
    # ================================
    total_pontos = 250_000_000
    n_processos = 4
    pontos_por_processo = total_pontos // n_processos

    inicio_paralelo = time.time()
    with Pool(n_processos) as pool:
        resultados = pool.map(contar_pontos_circulo, [pontos_por_processo]*n_processos)

    dentro_circulo_total = sum(resultados)
    pi_paralelo = 4 * dentro_circulo_total / total_pontos
    fim_paralelo = time.time()

    print(f"π ≈ {pi_paralelo} (paralelo)")
    print(f"Tempo paralelo: {fim_paralelo - inicio_paralelo:.2f} segundos")

    # ================================
    # SERIAL
    # ================================
    total_pontos_serial = 250_000_000

    inicio_serial = time.time()
    dentro_circulo_total_serial = contar_pontos_circulo(total_pontos_serial)
    pi_serial = 4 * dentro_circulo_total_serial / total_pontos_serial
    fim_serial = time.time()

    print(f"π ≈ {pi_serial} (serial)")
    print(f"Tempo serial: {fim_serial - inicio_serial:.2f} segundos")
