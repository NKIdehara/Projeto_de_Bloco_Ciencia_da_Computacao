class MinHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, valor):
        self.heap.append(valor)
        self._heap_up(len(self.heap) - 1)

    def _heap_up(self, index):
        pai = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[pai]:
            self.heap[index], self.heap[pai] = self.heap[pai], self.heap[index]
            index = pai
            pai = (index - 1) // 2

    def _heap_down(self, index):
        min = index
        esquerda = 2 * index + 1
        direita = 2 * index + 2

        if esquerda < len(self.heap) and self.heap[esquerda] < self.heap[min]:
            min = esquerda
        if direita < len(self.heap) and self.heap[direita] < self.heap[min]:
            min = direita

        if min != index:
            self.heap[index], self.heap[min] = self.heap[min], self.heap[index]
            self._heap_down(min)

    def imprimir(self):
        return self.heap

    def buscar(self, valor):
        return valor in self.heap

    def remover(self, valor):
        if valor in self.heap:
            index = self.heap.index(valor)
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            if index < len(self.heap):
                self._heap_down(index)
                self._heap_up(index)

# (1)
lista = [5, 2, 3, 7, 1]
heap = MinHeap()
for i in lista:
    heap.inserir(i)
print(f"Heap: {heap.imprimir()}")

# (2)
valor = 0
heap.inserir(valor)
print(f"Heap com {valor} inserido: {heap.imprimir()}")

# (3)
valor = 7
print(f"Elemento {valor} no heap: {heap.buscar(valor)}")

# (4)
valor = 0
heap.remover(valor)
print(f"Heap com {valor} removido: {heap.imprimir()}")
