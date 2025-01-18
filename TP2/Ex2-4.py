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

def mediana(lista):
    n = len(lista)
    if n % 2 == 1: # lista possui número impar de elementos
        return quick_select(lista, n // 2)
    else:          # lista possui número par de elementos
        return (quick_select(lista, n // 2 -1) + quick_select(lista, n // 2)) / 2


def quick_select_k_menores(lista, posicao):
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
        return quick_select_k_menores(sublista1, posicao)
    elif posicao < len(sublista1) + len(sublista2):
        return sublista1 + sublista2
    else:
        return sublista1 + sublista2 + quick_select_k_menores(sublista3, posicao - len(sublista1) - len(sublista2))


lista = [9, 1, 1, 9, 4, 7, 9, 5, 2, 4, 1, 6, 2, 5, 0, 8]
print(f"o valor da mediana é: {mediana(lista)}")
print(quick_select_k_menores(lista, 5))