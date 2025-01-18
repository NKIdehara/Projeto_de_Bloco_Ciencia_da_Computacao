import time
import random

def mochila_memorizacao(capacidade, pesos, itens, n, memoria):
    # implementação de memorização / consulta memória
    if (capacidade, n) in memoria:
        return memoria[(capacidade, n)]
    
    if n == 0 or capacidade == 0:
        return 0
    if (pesos[n-1] > capacidade):
        return mochila_memorizacao(capacidade, pesos, itens, n-1, memoria)
    else:
        resultado = max(itens[n-1] + mochila_memorizacao(capacidade-pesos[n-1], pesos, itens, n-1, memoria), mochila_memorizacao(capacidade, pesos, itens, n-1, memoria))
    
    # implementação de memorização / armazena memória
    memoria[(capacidade, n)] = resultado
    return resultado

pesos = []
itens = []
for i in range(0, 1001):
    pesos = pesos + [random.randint(1, 99) for _ in range(1)]
    itens = itens + [random.randint(1, 20) for _ in range(1)]
    capacidade = 150
    t_ini = time.time()
    resultado = mochila_memorizacao(capacidade, pesos, itens, len(pesos), {})
    t_fim = time.time()
    print(f"Num. elementos: {len(pesos)}\tTempo: {(t_fim - t_ini):.2f}\tResultado: {resultado}")
