def soma_moedas(moedas):
    return

def minimo_moedas(valor, moedas, conjunto, memoria):
    if len(moedas) == 0:
        return
    for i in range(len(moedas)):
        sequencia = conjunto[:]
        sequencia.append(moedas[i])
        if tuple(sequencia) in memoria:
            return memoria[sequencia]
        if sum(sequencia) == valor:
            memoria[tuple(sequencia)] = len(sequencia)
        if sum(sequencia) < valor:
            minimo_moedas(valor, moedas, sequencia, memoria) # armazena na memória a quantidade de moedas
    return min(memoria.values())

moedas = [1, 2, 5]
valor = 7
memoria = {}
temp = minimo_moedas(valor, moedas, [], memoria)
conjunto_moedas = [key for key in memoria if memoria[key] == temp]
print(f"As possibilidades de troco para um valor de {valor} com menor número de moedas de {moedas} é: {conjunto_moedas}, com {len(conjunto_moedas[0])} moedas")

moedas = [1, 2, 5]
valor = 11
memoria = {}
temp = minimo_moedas(valor, moedas, [], memoria)
conjunto_moedas = [key for key in memoria if memoria[key] == temp]
print(f"As possibilidades de troco para um valor de {valor} com menor número de moedas de {moedas} é: {conjunto_moedas}, com {len(conjunto_moedas[0])} moedas")

moedas = [1, 2, 5]
valor = 20
memoria = {}
temp = minimo_moedas(valor, moedas, [], memoria)
conjunto_moedas = [key for key in memoria if memoria[key] == temp]
print(f"As possibilidades de troco para um valor de {valor} com menor número de moedas de {moedas} é: {conjunto_moedas}, com {len(conjunto_moedas[0])} moedas")

moedas = [1, 2, 5]
valor = 21
memoria = {}
temp = minimo_moedas(valor, moedas, [], memoria)
conjunto_moedas = [key for key in memoria if memoria[key] == temp]
print(f"As possibilidades de troco para um valor de {valor} com menor número de moedas de {moedas} é: {conjunto_moedas}, com {len(conjunto_moedas[0])} moedas")
