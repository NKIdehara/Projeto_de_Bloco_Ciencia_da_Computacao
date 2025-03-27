def bubble_sort(itens):
    for i in range(len(itens)):
        for j in range(0, len(itens) - i - 1):
            peso1, valor1 = itens[j]
            peso2, valor2 = itens[j + 1]
            if (valor1 / peso1) < (valor2 / peso2): # critério de ordenação: valor/peso
                itens[j], itens[j + 1] = itens[j + 1], itens[j]
    return itens

def mochila_gulosa(capacidade, itens):
    bubble_sort(itens)
    valor_total = 0
    peso_total = 0
    itens_mochila = []
    for peso, valor in itens:
        if peso_total + peso <= capacidade:
            peso_total += peso
            valor_total += valor
            itens_mochila.append((peso, valor))
    return valor_total, itens_mochila

# (peso, valor)
itens = [(2, 40), (3, 50), (5, 100), (4, 90)]
capacidade = 8

valor_total, selecionados = mochila_gulosa(capacidade, itens)
for i, (peso, valor_total) in enumerate(selecionados):
    print(f"item {i}: peso {peso}, valor {valor_total}")
print("Valor total:", valor_total)
