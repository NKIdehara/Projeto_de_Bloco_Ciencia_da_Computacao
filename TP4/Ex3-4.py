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

    def dfs_recursivo(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()
        print(vertice, end=" -> ")
        visitados.add(vertice)
        for vizinho in self.lista[vertice]:
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)

    def bfs(self, inicio):
        visitados = set()
        fila = [inicio]
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                print(vertice, end=" -> ")
                visitados.add(vertice)
                fila.extend(self.lista[vertice])

    def buscar_caminho_bfs(self, inicio, fim):
        visitados = set()
        fila = [[inicio]]
        while fila:
            caminho = fila.pop(0)
            vertice = caminho[-1]
            if vertice  == fim:
                return caminho
            if vertice not in visitados:
                visitados.add(vertice)
                for vizinho in self.lista[vertice]:
                    novo_caminho = list(caminho)
                    novo_caminho.append(vizinho)
                    fila.append(novo_caminho)
        return

grafo = Grafo()

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
for a1, a2 in arestas:
    grafo.adicionar_aresta(a1, a2)

print("(3-1)")
print("Lista de Adjacência:")
grafo.mostrar_grafo()

print("\n(3-2)")
aresta = "A"
print(f"DFS a partir de {aresta}: ", end="")
grafo.dfs_recursivo(aresta)
print("\n\n(3-3)")
print(f"BFS a partir de {aresta}: ", end="")
grafo.bfs(aresta)

inicio = "A"
fim = "E"
print("\n\n(3-4)")
print(f"Caminho mais curto de {inicio} para {fim}: {grafo.buscar_caminho_bfs(inicio, fim)}")
