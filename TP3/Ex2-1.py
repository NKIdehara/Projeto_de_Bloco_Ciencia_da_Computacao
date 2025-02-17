import time
import multiprocessing

def calcular_soma(lista):
    return sum(lista)

def dividir_lista(lista, num_partes):
    tamanho = len(lista)
    return [lista[i * tamanho // num_partes: (i + 1) * tamanho // num_partes] for i in range(num_partes)]

def soma_paralela(lista, num_nucleos):
    partes = dividir_lista(lista, num_nucleos)
    with multiprocessing.Pool(num_nucleos) as pool:
        resultados = pool.map(calcular_soma, partes)
    return sum(resultados)

if __name__ == "__main__":
    lista_numeros = [i for i in range(1, 10_000_001)]
    num_nucleos = multiprocessing.cpu_count()

    for i in range(1, num_nucleos+1):
        t_ini = time.time()
        soma_total = soma_paralela(lista_numeros, num_nucleos)
        t_fim = time.time()
        print(f"Núcleos: {i}\tSoma total: {soma_total}\tTempo: {(t_fim - t_ini):.2f}")
