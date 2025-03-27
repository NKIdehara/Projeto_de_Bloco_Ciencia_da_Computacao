class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def adicionar_aresta(self, aresta1, aresta2, peso):
        self.vertices[aresta1][aresta2] = peso
        self.vertices[aresta2][aresta1] = peso

    def dijkstra(self, origem, destino):
        nao_visitados = list(self.vertices.keys())
        pesos = {vertice: float("inf") for vertice in self.vertices}
        pesos[origem] = 0
        predecessores = {}
        while nao_visitados:
            vertice_atual = min(nao_visitados, key=lambda vertice: pesos[vertice])
            if pesos[vertice_atual] == float("inf"):
                break
            for vizinho, peso in self.vertices[vertice_atual].items():
                novo_peso = pesos[vertice_atual] + peso
                if novo_peso < pesos[vizinho]:
                    pesos[vizinho] = novo_peso
                    predecessores[vizinho] = vertice_atual
            nao_visitados.remove(vertice_atual)
        caminho = []
        vertice_atual = destino
        while vertice_atual in predecessores:
            caminho.append(vertice_atual)
            vertice_atual = predecessores[vertice_atual]
        caminho.append(origem)
        caminho.reverse()
        return caminho, pesos[destino]

    def mostrar_grafo(self):
        for bairro, rotas in self.vertices.items():
            conexoes = ", ".join(f"({vizinho}, {dist})" for vizinho, dist in rotas.items())
            print(f"{bairro}: [{conexoes}]")

grafo = GrafoPoderado()
vertices = ["A", "B", "C", "D"]
for vertice in vertices:
    grafo.adicionar_vertice(vertice)
grafo.adicionar_aresta("A", "B", 1)
grafo.adicionar_aresta("A", "C", 4)
grafo.adicionar_aresta("B", "C", 2)
grafo.adicionar_aresta("B", "D", 5)
grafo.adicionar_aresta("C", "D", 1)

print("Grafo:")
grafo.mostrar_grafo()

print("\nDistancias:")
origem = "A"
for vertice in vertices:
    rota, distancia = grafo.dijkstra(origem, vertice)
    print(f"Distância até {vertice}: {distancia}\tMelhor rota de {origem} para {vertice}: {' => '.join(rota)}")
