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

    def pre_ordem(self):
        resultado = []
        self._pre_ordem(self.raiz, resultado)
        return resultado

    def _pre_ordem(self, no, resultado):
        if no:
            resultado.append(no.valor)
            self._pre_ordem(no.esquerda, resultado)
            self._pre_ordem(no.direita, resultado)

    def in_ordem(self):
        resultado = []
        self._in_ordem(self.raiz, resultado)
        return resultado

    def _in_ordem(self, no, resultado):
        if no:
            self._in_ordem(no.esquerda, resultado)
            resultado.append(no.valor)
            self._in_ordem(no.direita, resultado)

    def pos_ordem(self):
        resultado = []
        self._pos_ordem(self.raiz, resultado)
        return resultado

    def _pos_ordem(self, no, resultado):
        if no:
            self._pos_ordem(no.esquerda, resultado)
            self._pos_ordem(no.direita, resultado)
            resultado.append(no.valor)

arvore = Arvore()

arvore.inserir(57)
arvore.inserir(31)
arvore.inserir(48)
arvore.inserir(29)
arvore.inserir(94)
arvore.inserir(17)
print("Pré Ordem:", arvore.pre_ordem())
print("In Ordem:", arvore.in_ordem())
print("Pós Ordem:", arvore.pos_ordem())

print()

arvore2 = Arvore()
arvore2.inserir(50)
arvore2.inserir(30)
arvore2.inserir(70)
arvore2.inserir(20)
arvore2.inserir(40)
arvore2.inserir(60)
arvore2.inserir(80)
print("In Ordem:", arvore2.in_ordem())
print("Pré Ordem:", arvore2.pre_ordem())
print("Pós Ordem:", arvore2.pos_ordem())
