from multiprocessing import Pool
import time
import random

def max_parallel(lst, process):
    with Pool(process) as pool:
        chunk_size = len(lst) // process
        chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
        results = pool.map(max, chunks)
    return max(results)

def maximo(lista):
    resultado = 0
    for i in lista:
        if i > resultado:
            resultado = i
    return resultado

if __name__ == '__main__':
    for i in range(3, 26):
        lista = [random.randint(0, 2 ** 32) for _ in range(2 ** i)]
        print(f"Qtde: {len(lista)}", end="\t")
        t_1 = time.time()
        print(f"Max paralela: {max_parallel(lista, 5)}", end="\t")
        t_2 = time.time()
        print(f"Max sequencial: {maximo(lista)}", end="\t")
        t_3 = time.time()
        print(f"Tempo paralela: {(t_2 - t_1):.2f}\tTempo sequencial: {(t_3 - t_2):.2f}")