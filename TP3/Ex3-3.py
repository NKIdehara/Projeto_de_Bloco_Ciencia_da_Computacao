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

    def encontrar_maior_paralelo(self):
        return self._encontrar_maior_paralelo(self.raiz)

    def _encontrar_maior_paralelo(self, no):
        if no is None:
            return 0
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futuro_esquerda = executor.submit(self._encontrar_maior_paralelo, no.esquerda)
            futuro_direita = executor.submit(self._encontrar_maior_paralelo, no.direita)
            return max(no.valor, futuro_esquerda.result(), futuro_direita.result())

arvore = Arvore()
lista =  [15, 10, 20, 8, 12, 17, 25]
for i in lista:
    arvore.inserir(i)

print("In Ordem:", arvore.in_ordem())

maior_valor = arvore.encontrar_maior_paralelo()
print(f"Valoe maximo: {maior_valor}")