import multiprocessing
import random
import time

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

    def numero_nos(self):
        return self._conta_nos(self.raiz)

    def _conta_nos(self, no):
        if no is None:
            return 0
        return 1 + self._conta_nos(no.esquerda) + self._conta_nos(no.direita)

    def busca_paralela(self, valor):
        with multiprocessing.Pool(processes=2) as pool:
            return pool.apply_async(self._busca_paralela, (self.raiz, valor)).get()

    def _busca_paralela(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        valor_esquerda = valor_direita = False
        if no.esquerda:
            valor_esquerda = self._busca_paralela(no.esquerda, valor)
        if no.direita:
            valor_direita = self._busca_paralela(no.direita, valor)
        return valor_esquerda or valor_direita


if __name__ == "__main__":
    for i in range(21):
        arvore = Arvore()
        for j in range(2 ** i):
            arvore.inserir(random.randint(0, 1024))
        t_ini = time.time()
        valor = 64
        encontrado = arvore.busca_paralela(valor)
        t_fim = time.time()
        if encontrado:
            print(f"num. nós: {arvore.numero_nos()}\t{valor} encontrado\ttempo: {(t_fim - t_ini):.2f}")
        else:
            print(f"num. nós: {arvore.numero_nos()}\t{valor} não encontrado\ttempo: {(t_fim - t_ini):.2f}")
