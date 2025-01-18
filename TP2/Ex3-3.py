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

    def buscar_valor(self, valor):
        no = self.lista
        posicao = 0
        while no.proximo is not None and no.valor != valor:
            no = no.proximo
            posicao += 1
        if no.valor == valor:
            print(f"posição do valor {valor} = {posicao}")

    def inverter_lista(self):
        no = self.lista
        anterior = None
        while no is not None:
            proximo = no.proximo
            no.proximo = anterior
            anterior = no
            no = proximo
        self.lista = anterior

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
lista.buscar_valor(5)
lista.inverter_lista()
lista.exibir_elementos()
