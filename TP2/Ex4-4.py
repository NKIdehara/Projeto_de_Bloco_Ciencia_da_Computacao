def listar_permutacoes(string):
    caracteres = set(string)
    caracteres = list(caracteres)
    print(permutacoes(caracteres))

def permutacoes(lista):
    if len(lista) == 0:
        return [""]

    resposta = []
    for i in range(len(lista)):
        string_i = lista[i]
        string_restante = lista[:i] + lista[i+1:]

        combinacoes = permutacoes(string_restante)
        for combinacao in combinacoes:
            resposta.append(string_i + combinacao)

    return resposta

listar_permutacoes("teste")
# listar_permutacoes("rio de janeiro")