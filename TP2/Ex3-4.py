import random

class DNode:
    def __init__(self, valor):
        self.anterior = None
        self.valor = valor
        self.proximo = None

class DoublyLinkedList:
    def __init__(self):
        self.lista = None

    def inserir_inicio(self, valor):
        if self.lista is None:
            self.lista = DNode(valor)
        else:
            novo = DNode(valor)
            novo.proximo = self.lista
            self.lista.anterior = novo
            self.lista = novo

    def inserir_final(self, valor):
        if self.lista is None:
            self.lista = DNode(valor)
        else:
            no = self.lista
            while no.proximo is not None:
                no = no.proximo
            novo = DNode(valor)
            novo.anterior = no
            no.proximo = novo

    def excluir_valor(self, valor):
        if self.lista is None:
            return
        else:
            no = self.lista
            while no.proximo is not None and no.valor != valor:
                no = no.proximo
            if no.valor == valor:
                anterior = no.anterior
                anterior.proximo = no.proximo
                no.proximo.anterior = anterior

    def exibir_elementos(self):
        no = self.lista
        print(f"{no.valor:02}", end="")
        while no.proximo is not None:
            no = no.proximo
            print(f" <-> {no.valor:02}", end="")
        print(f"  |  {no.valor:02}", end="")
        while no.anterior is not None:
            no = no.anterior
            print(f" <-> {no.valor:02}", end="")
        print()

    def trocar_elementos(self, elemento1, elemento2):
        temp = elemento1.valor
        elemento1.valor = elemento2.valor
        elemento2.valor = temp

    def bubble_sort(self):
        no_i = self.lista
        while no_i.proximo is not None:
            no_j = self.lista
            while no_j.proximo is not None:
                if no_j.valor > no_j.proximo.valor:
                    self.trocar_elementos(no_j, no_j.proximo)
                no_j = no_j.proximo
            no_i = no_i.proximo

    def mesclar(self, linked_list):
        if linked_list is None:
            return
        else:
            no = self.lista
            while no.proximo is not None:
                no = no.proximo
            lista = linked_list.lista
            no.proximo = lista
            lista.anterior = no

lista = DoublyLinkedList()
for i in range(5):
    lista.inserir_inicio(random.randint(1, 30))

print("Lista 1 não ordenada: ", end="")
lista.exibir_elementos()
lista.bubble_sort()
print("Lista 1 ordenada:     ", end="")
lista.exibir_elementos()

lista_nova = DoublyLinkedList()
for i in range(5):
    lista_nova.inserir_inicio(random.randint(1, 30))
print("Lista 2: ", end="")
lista_nova.exibir_elementos()
print("Lista mesclada: ", end="")
lista_nova.mesclar(lista)
lista_nova.exibir_elementos()