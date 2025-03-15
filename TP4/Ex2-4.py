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

    def buscar(self, palavra):
        no = self.raiz
        for p in palavra:
            if p not in no.filhos: # caracter atual não faz parte da palavra
                return False
            no = no.filhos[p]
        return no.fim_palavra # encontrou palavra completa

    def imprimir(self, no=None, prefixo=""):
        if no is None:
            no = self.raiz
        if no.fim_palavra: # palavra completa
            print(f"Palavra: {prefixo}")
        for caracter, filho in no.filhos.items():
            self.imprimir(filho, prefixo + caracter) # junta caracteres de forma recursiva

    def autocompletar(self, prefixo):
        def _encontrar_no(no, prefixo): # encontrar começo do nó
            for p in prefixo:
                if p not in no.filhos:
                    return None
                no = no.filhos[p]
            return no
        def _coletar_nos(no, palavra, palavras): # junta os caracteres da palavra
            if no.fim_palavra:
                palavras.append(palavra) # palavra completa
            for caracter, filho in no.filhos.items():
                _coletar_nos(filho, palavra + caracter, palavras)
        palavras = []
        no = _encontrar_no(self.raiz, prefixo)
        if no:
            _coletar_nos(no, prefixo, palavras)
        return palavras

    def remover(self, palavra):
        def _remover(no, palavra, indice):
            if indice == len(palavra):
                if not no.fim_palavra:
                    return False  # Palavra não encontrada
                no.fim_palavra = False
                return len(no.filhos) == 0  # Remove nó se não tiver filhos
            caracter = palavra[indice]
            if caracter not in no.filhos:
                return False  # Palavra não encontrada
            pode_remover = _remover(no.filhos[caracter], palavra, indice + 1)
            if pode_remover:
                del no.filhos[caracter]
                return len(no.filhos) == 0 and not no.fim_palavra
            return False
        _remover(self.raiz, palavra, 0)

print("(2-1)")
lista = ["casa", "casamento", "casulo", "cachorro"]
trie = Trie()
for i in lista:
    trie.inserir(i)
trie.imprimir()

print("\n(2-2)")
palavra = "chocolate"
print(f"{palavra} está em Trie: {trie.buscar(palavra)}")
palavra = "casa"
print(f"{palavra} está em Trie: {trie.buscar(palavra)}")

print("\n(2-3)")
prefixo = "cas"
print(f"todas as palavras com o prefixo {prefixo}: {trie.autocompletar(prefixo)}")

print("\n(2-4)")
palavra = "casa"
print(f"removendo palavra \"{palavra}\"")
trie.remover(palavra)
trie.imprimir()
