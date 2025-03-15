class Grafo:
    def __init__(self):
        self.lista = {}

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 not in self.lista:
            self.lista[vertice1] = []
        if vertice2 not in self.lista:
            self.lista[vertice2] = []
        if vertice1 in self.lista and vertice2 in self.lista:
            self.lista[vertice1].append(vertice2)
            self.lista[vertice2].append(vertice1)

    def mostrar_grafo(self):
        for vertice in self.lista:
            print(f"{vertice} -> {self.lista[vertice]}")

grafo = Grafo()

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
for a1, a2 in arestas:
    grafo.adicionar_aresta(a1, a2)

print("Lista de Adjacência:")
grafo.mostrar_grafo()
