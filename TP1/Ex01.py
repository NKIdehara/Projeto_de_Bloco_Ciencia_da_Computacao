import time
from memory_profiler import memory_usage

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort(lista):
    for i in range(len(lista)):
        indice = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice]:
                indice = j
        lista[i], lista[indice] = lista[indice], lista[i]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        item = lista[i]
        for j in range(i):
            if lista[j] > item:
                lista[j + 1 : i + 1] = lista[j:i] # move bloco de itens da lista
                lista[j] = item
                break
    return lista

def ler_arquivo(lista):
    with open("./arquivo_saida.txt", 'r') as file:
        linhas = file.read().splitlines()
        for linha in enumerate(linhas):
            lista.append(linha)

def calcula_tempo(func, lista):
    resultado = []
    t_ini = time.time()
    m_ini = memory_usage()[0]
    resultado = func(lista)
    t_fim = time.time()
    m_fim = memory_usage()[0]
    print(f"Tempo de execução de {func.__name__}: {(t_fim - t_ini):.2f} s\tMemória usada: {m_fim - m_ini} MiB")
    return resultado

lista = []
ler_arquivo(lista)
# print(bubble_sort(lista))
# print(selection_sort(lista))
# print(insertion_sort(lista))
calcula_tempo(bubble_sort, lista)
ler_arquivo(lista)
calcula_tempo(selection_sort, lista)
ler_arquivo(lista)
calcula_tempo(insertion_sort, lista)