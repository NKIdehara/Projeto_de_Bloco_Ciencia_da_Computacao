import concurrent.futures

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir(no.direita, valor)

    def in_ordem(self):
        resultado = []
        self._in_ordem(self.raiz, resultado)
        return resultado

    def _in_ordem(self, no, resultado):
        if no:
            self._in_ordem(no.esquerda, resultado)
            resultado.append(no.valor)
            self._in_ordem(no.direita, resultado)

    def busca_dfs_paralela(self, alvo):
        return self._busca_dfs_paralela(self.raiz, alvo, [])

    def _busca_dfs_paralela(self, no, alvo, caminho):
        if no is None:
            return None
        novo_caminho = caminho + [no.valor]
        if no.valor == alvo:
            return novo_caminho
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futuro_esquerda = executor.submit(self._busca_dfs_paralela, no.esquerda, alvo, novo_caminho)
            futuro_direita = executor.submit(self._busca_dfs_paralela, no.direita, alvo, novo_caminho)
            resultado_esquerda = futuro_esquerda.result()
            resultado_direita = futuro_direita.result()
            return resultado_esquerda or resultado_direita

arvore = Arvore()
lista = [i for i in range(1, 10)]
for i in lista:
    arvore.inserir(i)
caminho = arvore.busca_dfs_paralela(5)
print("In Ordem:", arvore.in_ordem())

if caminho:
    print(f"Caminho até o nó 5: {caminho}")
else:
    print("Nó não encontrado na árvore.")