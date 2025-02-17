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

    def verificar_bst(self):
        if self.raiz is None:
            return True
        esquerda = True
        direita = True
        if self.raiz.esquerda is not None:
            esquerda = self._verificar_esquerda(self.raiz.esquerda, self.raiz.valor)
        if self.raiz.direita is not None:
            direita = self._verificar_direita(self.raiz.direita, self.raiz.valor)
        return esquerda and direita

    def _verificar_esquerda(self, no, limite):
        if no is None:
            return True
        if no.valor > limite:
            return False
        esquerda = True
        direita = True
        if no.esquerda is not None:
            esquerda = self._verificar_esquerda(no.esquerda, no.valor)
        if no.direita is not None:
            direita = self._verificar_direita(no.direita, no.valor)
        return esquerda and direita

    def _verificar_direita(self, no, limite):
        if no is None:
            return True
        if no.valor < limite:
            return False
        esquerda = True
        direita = True
        if no.esquerda is not None:
            esquerda = self._verificar_esquerda(no.esquerda, no.valor)
        if no.direita is not None:
            direita = self._verificar_direita(no.direita, no.valor)
        return esquerda and direita

    def trocar_valor(self, original, novo):
        return self._buscar(self.raiz, original, novo)

    def _buscar(self, no, original, novo):
        if no is None:
            return no
        if no.valor == original:
            no.valor = novo
        if original < no.valor:
            return self._buscar(no.esquerda, original, novo)
        else:
            return self._buscar(no.direita, original, novo)


arvore = Arvore()
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)
print("In Ordem:", arvore.in_ordem())
print(f"BST: {arvore.verificar_bst()}")

arvore.trocar_valor(40, 15)
print("valor trocado: 40 -> 15")

print("In Ordem:", arvore.in_ordem())
print(f"BST: {arvore.verificar_bst()}")
