import multiprocessing
import sys
sys.setrecursionlimit(100000)

def num_primo(n, divisor=2):
    if n < 2:
        return False
    if divisor > n // 2:
        return True
    if n % divisor == 0:
        return False
    return num_primo(n, divisor + 1)

def contar_primos(intervalo):
    return sum(1 for n in intervalo if num_primo(n))

def intervalo(inicio, final, num_partes):
    tamanho = (final - inicio) // num_partes
    return [(inicio + i * tamanho, inicio + (i + 1) * tamanho) for i in range(num_partes - 1)] + [(inicio + (num_partes - 1) * tamanho, final)]

def contar_primos_paralelo(inicio, final, num_processos):
    intervalos = intervalo(inicio, final, num_processos)
    intervalos_lista = [list(range(ini, fim)) for ini, fim in intervalos]
    with multiprocessing.Pool(num_processos) as pool:
        resultados = pool.map(contar_primos, intervalos_lista)
    return sum(resultados)

if __name__ == "__main__":
    inicio = 1
    final = 100_000
    num_processos = multiprocessing.cpu_count()
    quantidade_primos = contar_primos_paralelo(inicio, final, num_processos)
    print(f"Quantidade de números primos entre {inicio} e {final}: {quantidade_primos}")