import multiprocessing
import random
import time

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    elemento_pivo = lista[len(lista) // 2]
    sublista1 = []
    for i in lista:
        if i < elemento_pivo:
            sublista1.append(i)
    sublista2 = []
    for i in lista:
        if i == elemento_pivo:
            sublista2.append(i)
    sublista3 = []
    for i in lista:
        if i > elemento_pivo:
            sublista3.append(i)
    return quick_sort(sublista1) + sublista2 + quick_sort(sublista3)

def quick_sort_paralelo(lista):
    if len(lista) <= 1:
        return lista
    elemento_pivo = lista[len(lista) // 2]
    sublista1 = []
    for i in lista:
        if i < elemento_pivo:
            sublista1.append(i)
    sublista2 = []
    for i in lista:
        if i == elemento_pivo:
            sublista2.append(i)
    sublista3 = []
    for i in lista:
        if i > elemento_pivo:
            sublista3.append(i)
    with multiprocessing.Pool(processes=5) as pool:
        sublista1, sublista3 = pool.map(quick_sort, [sublista1, sublista3])
    return sublista1 + sublista2 + sublista3

if __name__ == "__main__":
    for i in range(26):
        lista = [random.randint(0, 2048) for _ in range(2 ** i)]
        t_1 = time.time()
        quick_sort(lista)
        t_2 = time.time()
        quick_sort_paralelo(lista)
        t_3 = time.time()
        print(f"itens: {len(lista)}\tsequencial: {(t_2 - t_1):.2f}\tquick sort paralelo: {(t_3 - t_2):.2f}")
