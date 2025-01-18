# Exercício 5.1: Soma de Elementos em uma Lista
from multiprocessing import Pool
import time
import random

def sum_parallel(lst, process):
    with Pool(process) as pool:
        chunk_size = len(lst) // process
        chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
        results = pool.map(sum, chunks)
    return sum(results)

def soma(lista):
    resultado = 0
    for i in lista:
        resultado += i
    return resultado

if __name__ == '__main__':
    for i in range(100000, 10000001, 10000):
        large_list = [random.randint(1, 99) for _ in range(i)]
        print(f"Qtde: {len(large_list)}", end="\t")
        t_1 = time.time()
        print(f"Soma paralela: {sum_parallel(large_list, 10)}", end="\t")
        t_2 = time.time()
        print(f"Soma sequencial: {soma(large_list)}", end="\t")
        t_3 = time.time()
        print(f"Tempo paralela: {(t_2 - t_1):.2f}\tTempo sequencial: {(t_3 - t_2):.2f}")