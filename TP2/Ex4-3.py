import time

def nome_pilha(pilha):
    return [n for n, valor in globals().items() if valor is pilha][0]

def mover_peca(origem, destino):
    peca = origem.pop()
    destino.append(peca)
    return peca

def torre_hanoi_movimento(n, origem, auxiliar, destino):
    if n == 1:
        peca = mover_peca(origem, destino)
        print(f"movendo peça {peca}: {nome_pilha(origem)} -> {nome_pilha(destino)}")
        return
    torre_hanoi_movimento(n-1, origem, destino, auxiliar) # (1)
    peca = mover_peca(origem, destino)          # (2)
    print(f"movendo peça {peca}: {nome_pilha(origem)} -> {nome_pilha(destino)}")
    torre_hanoi_movimento(n-1, auxiliar, origem, destino) # (3)

def torre_hanoi(n, origem, auxiliar, destino):
    if n == 1:
        peca = mover_peca(origem, destino)
        return
    torre_hanoi(n-1, origem, destino, auxiliar) # (1)
    peca = mover_peca(origem, destino)          # (2)
    torre_hanoi(n-1, auxiliar, origem, destino) # (3)

origem = ['A', 'B', 'C']
auxiliar = []
destino = []
torre_hanoi_movimento(len(origem), origem, auxiliar, destino)

# pecas = []
# for i in range(65, 95):
#     pecas.append(chr(i))
#     origem = pecas[:]
#     auxiliar = []
#     destino = []
#     tempo = time.time()
#     torre_hanoi(len(origem), origem, auxiliar, destino)
#     print(f"número de peças: {len(destino)}\ttempo: {(time.time()-tempo):.5f}")
