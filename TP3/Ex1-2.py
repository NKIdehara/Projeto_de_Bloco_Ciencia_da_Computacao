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

    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, no, valor):
        if no is None: # nó inexistente
            return no
        if valor < no.valor: # remover valor à esquerda
            no.esquerda = self._remover(no.esquerda, valor)
        elif valor > no.valor: # remover valor à direita
            no.direita = self._remover(no.direita, valor)
        else: # remover nó
            if no.esquerda is None and no.direita is None: # nó sem filhos
                return None
            elif no.esquerda is None: # nó com 1 filho (filho à direita)
                return no.direita
            elif no.direita is None: # nó com 1 filho (filho à esquerda)
                return no.esquerda
            else: # nó com dois filhos
                escolhido = self._minimo(no.direita)
                no.valor = escolhido.valor
                no.direita = self._remover(no.direita, escolhido.valor)
        return no

    def _minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

arvore = Arvore()
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)
print("In Ordem:", arvore.in_ordem())

arvore.remover(20)
print("In Ordem:", arvore.in_ordem())
arvore.remover(30)
print("In Ordem:", arvore.in_ordem())
arvore.remover(50)
print("In Ordem:", arvore.in_ordem())
