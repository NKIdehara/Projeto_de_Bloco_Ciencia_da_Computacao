class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.lista = None

    def inserir_inicio(self, valor):
        if self.lista is None:
            self.lista = Node(valor)
        else:
            novo = Node(valor)
            novo.proximo = self.lista
            self.lista = novo

    def inserir_final(self, valor):
        if self.lista is None:
            self.lista = Node(valor)
        else:
            no = self.lista
            while no.proximo is not None:
                no = no.proximo
            no.proximo = Node(valor)

    def excluir_valor(self, valor):
        if self.lista is None:
            return
        else:
            no = self.lista
            while no.proximo is not None and no.valor != valor:
                anterior = no
                no = no.proximo
            if no.valor == valor:
                anterior.proximo = no.proximo

    def exibir_elementos(self):
        no = self.lista
        print(f"{no.valor}", end="")
        while no.proximo is not None:
            no = no.proximo
            print(f" -> {no.valor}", end="")
        print()

lista = LinkedList()
lista.inserir_inicio(5)
lista.inserir_inicio(4)
lista.inserir_inicio(3)
lista.inserir_final(6)
lista.inserir_final(7)
lista.exibir_elementos()
lista.excluir_valor(4)
lista.exibir_elementos()
lista.inserir_inicio(2)
lista.inserir_inicio(1)
lista.exibir_elementos()
