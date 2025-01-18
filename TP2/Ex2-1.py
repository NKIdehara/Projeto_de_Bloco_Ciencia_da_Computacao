import time
import random

def quick_sort(lista, opcao):
    if len(lista) <= 1:
        return lista

    if opcao == 0:
        elemento_pivo = 0
    elif opcao == 1:
        elemento_pivo = len(lista) // 2
    else:
        elemento_pivo = len(lista) - 1

    pivo = lista[elemento_pivo]
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
    return quick_sort(sublista1, opcao) + sublista2 + quick_sort(sublista3, opcao)



lista = [random.randint(0, 100000) for _ in range(1000000)]
t_1 = time.time()
quick_sort(lista[:], 0)
t_2 = time.time()
print(f"pivo: primeiro elemento\ttempo: {(t_2 - t_1):.2f}")
quick_sort(lista[:], 1)
t_3 = time.time()
print(f"pivo: elemento mediano\ttempo: {(t_3 - t_2):.2f}")
quick_sort(lista[:], 2)
t_4 = time.time()
print(f"pivo: ultimo elemento\ttempo: {(t_4 - t_3):.2f}")