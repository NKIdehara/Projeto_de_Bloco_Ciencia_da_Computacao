class GrafoAlgoritmoPrim:
    def __init__(self, vertices):
        self.vertices = vertices
        self.V = len(vertices)
        self.grafo = {vertice: {} for vertice in vertices}

    def adicionar_aresta(self, u, v, peso):
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso

    def prim(self):
        infinito = float('inf')
        selecionado = {vertice: False for vertice in self.vertices}
        chave = {vertice: infinito for vertice in self.vertices}
        pai = {vertice: None for vertice in self.vertices}
        chave[self.vertices[0]] = 0
        for _ in range(self.V):
            u = min((v for v in self.vertices if not selecionado[v]), key=lambda v: chave[v], default=None)
            if u is None:
                break
            selecionado[u] = True
            for v, peso in self.grafo[u].items():
                if not selecionado[v] and peso < chave[v]:
                    chave[v] = peso
                    pai[v] = u

        print("Arestas da Árvore Geradora Mínima:")
        custo_total = 0
        for v in self.vertices[1:]:
            if pai[v] is not None:
                print(f"{pai[v]} - {v} com peso {self.grafo[v][pai[v]]}")
                custo_total += self.grafo[v][pai[v]]
        print(f"\nCusto total da AGM: {custo_total}")

vertices = ["A", "B", "C", "D"]
grafo = GrafoAlgoritmoPrim(vertices)
grafo.adicionar_aresta("A", "B", 2)
grafo.adicionar_aresta("A", "C", 3)
grafo.adicionar_aresta("B", "C", 1)
grafo.adicionar_aresta("B", "D", 4)
grafo.adicionar_aresta("C", "D", 5)
grafo.prim()
