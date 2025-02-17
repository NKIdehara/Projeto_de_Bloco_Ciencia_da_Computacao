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

    def busca_paralela(self, alvo):
        return self._busca_paralela(self.raiz, alvo)

    def _busca_paralela(self, no, alvo):
        if no is None:
            return False
        if no.valor == alvo:
            return True
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futuro_esquerda = executor.submit(self._busca_paralela, no.esquerda, alvo)
            futuro_direita = executor.submit(self._busca_paralela, no.direita, alvo)
            return futuro_esquerda.result() or futuro_direita.result()

arvore = Arvore()
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

valor = 60
encontrado = arvore.busca_paralela(valor)
if encontrado:
    print(f"valor: {valor} - nó encontrado")
else:
    print(f"valor: {valor} - nó não encontrado")

valor = 61
encontrado = arvore.busca_paralela(valor)
if encontrado:
    print(f"valor: {valor} - nó encontrado")
else:
    print(f"valor: {valor} - nó não encontrado")