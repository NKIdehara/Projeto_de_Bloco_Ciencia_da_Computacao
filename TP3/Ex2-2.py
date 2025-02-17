import multiprocessing

def multiplicar_linha(args):
    linha, matriz_b_transposta = args
    resultado = [sum(linha[i] * matriz_b_transposta[j][i] for i in range(len(linha))) for j in range(len(matriz_b_transposta[0]))]
    return resultado

def multiplicacao_paralela(matriz_a, matriz_b):
    num_processos = len(matriz_a)
    matriz_b_transposta = [[matriz_b[j][i] for j in range(len(matriz_b))] for i in range(len(matriz_b[0]))]
    with multiprocessing.Pool(num_processos) as pool:
        resultado = pool.map(multiplicar_linha, [(linha, matriz_b_transposta) for linha in matriz_a])
    return resultado

if __name__ == "__main__":
    matriz_a = [[6, 1, 2],
                [4, 8, 7],
                [9, 4, 5]]

    matriz_b = [[7, 5, 3],
                [4, 1, 4],
                [9, 1, 8]]

    resultado = multiplicacao_paralela(matriz_a, matriz_b)

    print("Matriz A:")
    for linha in matriz_a:
        print(linha)

    print("\nMatriz B:")
    for linha in matriz_b:
        print(linha)

    print("\nResultado da multiplicação das matrizes:")
    for linha in resultado:
        print(linha)
