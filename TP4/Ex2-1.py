class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False

class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra):
        no = self.raiz
        for p in palavra:
            if p not in no.filhos:
                no.filhos[p] = NoTrie()
            no = no.filhos[p]
        no.fim_palavra = True

    def imprimir(self, no=None, prefixo=""):
        if no is None:
            no = self.raiz
        if no.fim_palavra: # palavra completa
            print(f"Palavra: {prefixo}")
        for caracter, filho in no.filhos.items():
            self.imprimir(filho, prefixo + caracter) # junta caracteres de forma recursiva

lista = ["casa", "casamento", "casulo", "cachorro"]
trie = Trie()
for i in lista:
    trie.inserir(i)
trie.imprimir()
