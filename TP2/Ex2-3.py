import time
import random

def quick_select(lista, posicao):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    sublista1 = []
    for i in lista:
        if i < pivo:
            sublista1.append(i)
    sublista2 = []
    for i in lista:
        if i == pivo:
            sublista2.append(i)
    sublista3 = []
    for i in lista:
        if i > pivo:
            sublista3.append(i)

    if posicao < len(sublista1):
        return quick_select(sublista1, posicao)
    elif posicao < len(sublista1) + len(sublista2):
        return pivo
    else:
        return quick_select(sublista3, posicao - len(sublista1) - len(sublista2))

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    sublista1 = []
    for i in lista:
        if i < pivo:
            sublista1.append(i)
    sublista2 = []
    for i in lista:
        if i == pivo:
            sublista2.append(i)
    sublista3 = []
    for i in lista:
        if i > pivo:
            sublista3.append(i)
    return quick_sort(sublista1) + sublista2 + quick_sort(sublista3)

lista_k = [600, 1200, 5000, 7500, 9999]
for i in range(5):
    for j in range(10):
        lista = [random.randint(1, 1000) for _ in range(10000)]
        posicao = lista_k[i]
        tempo = time.time()
        print(f"posição k: {posicao}\tk-ésimo menor elemento: {quick_select(lista, posicao)}\ttempo: {(time.time()-tempo):.5f}")
