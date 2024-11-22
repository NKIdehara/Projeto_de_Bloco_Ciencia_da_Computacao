import time
from memory_profiler import memory_usage

class Hashtable:
    def __init__(self):
        self.table = {}

    def inserir(self, chave: int, valor: str):
        self.table[chave] = valor

    def inserir_posicao(self, posicao: int, valor: str):
        t_ini = time.time()
        m_ini = memory_usage()[0]
        self.inserir(posicao, valor)
        return (memory_usage()[0] - m_ini), (time.time() - t_ini)

    def remover(self, chave: int):
        if chave in self.table:
            del self.table[chave]

    def remover_posicao(self, posicao: int):
        t_ini = time.time()
        m_ini = memory_usage()[0]
        self.remover(posicao)
        return (memory_usage()[0] - m_ini), (time.time() - t_ini)

    def valor(self, chave: int):
        return self.table[chave]

    def valor_posicao(self, posicao: int):
        t_ini = time.time()
        m_ini = memory_usage()[0]
        chaves = list(self.table.keys())
        if 0 <= posicao < len(chaves):
            return self.table[chaves[posicao]], (memory_usage()[0] - m_ini), (time.time() - t_ini)
        return None, (memory_usage()[0] - m_ini), (time.time() - t_ini)

    def tamanho(self):
        return len(self.table)

class Pilha:
    def __init__(self):
        self.pilha = []

    def inserir(self, valor: str):
        self.pilha.append(valor)

    def inserir_posicao(self, posicao: int, valor: str):
        t_ini = time.time()
        m_ini = memory_usage()[0]
        aux = self.pilha[:]
        for i in range(self.tamanho() - posicao):
            self.pilha.pop()
        self.pilha.append(valor)
        for i in range(posicao, len(aux)):
            self.pilha.append(aux[i])
        return (memory_usage()[0] - m_ini), (time.time() - t_ini)

    def remover(self):
        if len(self.pilha) > 0:
            return self.pilha.pop()
        return None

    def remover_posicao(self, posicao: int):
        t_ini = time.time()
        m_ini = memory_usage()[0]
        aux = self.pilha[:]
        for i in range(self.tamanho() - posicao):
            self.pilha.pop()
        for i in range(posicao + 1, len(aux)):
            self.pilha.append(aux[i])
        return (memory_usage()[0] - m_ini), (time.time() - t_ini)

    # cria pilha auxiliar e remove todos até chegar à posição
    def valor_posicao(self, posicao: int):
        t_ini = time.time()
        m_ini = memory_usage()[0]
        aux = self.pilha[:]
        for i in range(self.tamanho() - posicao - 1):
            aux.pop()
        if len(aux) > 0:
            return aux[-1], (memory_usage()[0] - m_ini), (time.time() - t_ini)
        return None, (memory_usage()[0] - m_ini), (time.time() - t_ini)

    def valor_posicao_lista(self, posicao: int):
        if 0 <= posicao < len(self.pilha):
            return self.pilha[posicao]
        return None

    def tamanho(self):
        return len(self.pilha)

    def imprimir(self):
        for i in range(len(self.pilha)):
            print(f"{self.pilha[i]} ", end="")
        print("")

class Fila:
    def __init__(self):
        self.fila = []

    def inserir(self, valor: str):
        self.fila.append(valor)

    def inserir_posicao(self, posicao: int, valor: str):
        t_ini = time.time()
        m_ini = memory_usage()[0]
        aux = []
        for i in range(self.tamanho() - posicao):
            aux.append(self.fila[i])
        aux.append(valor)
        for i in range(posicao, len(self.fila)):
            aux.append(self.fila[i])
        self.fila = aux
        return (memory_usage()[0] - m_ini), (time.time() - t_ini)

    def remover(self):
        if len(self.fila) > 0:
            return self.fila.pop(0)
        return None

    def remover_posicao(self, posicao: int):
        t_ini = time.time()
        m_ini = memory_usage()[0]
        aux = []
        for i in range(self.tamanho() - posicao - 1):
            aux.append(self.fila[i])
        for i in range(posicao + 1, len(self.fila)):
            aux.append(self.fila[i])
        self.fila = aux
        return (memory_usage()[0] - m_ini), (time.time() - t_ini)

    # cria fila auxiliar e remove todos até chegar à posição
    def valor_posicao(self, posicao: int):
        inicio = time.time()
        mem_inicio = memory_usage()[0]
        aux = self.fila[:]
        for i in range(posicao):
            aux.pop(0)
        if len(aux) > 0:
            return aux[0], (memory_usage()[0] - mem_inicio), (time.time() - inicio)
        return None, (memory_usage()[0] - mem_inicio), (time.time() - inicio)

    def valor_posicao_lista(self, posicao: int):
        if 0 <= posicao < len(self.fila):
            return self.fila[posicao]
        return None

    def tamanho(self):
        return len(self.fila)

    def imprimir(self):
        for i in range(len(self.fila)):
            print(f"{self.fila[i]} ", end="")
        print("")


def ler_arquivo(hashtable, pilha, fila):
    with open("./arquivo_saida.txt", "r") as arq:
        linhas = arq.read().splitlines()
        for i, linha in enumerate(linhas):
            hashtable.inserir(i, linha)
            pilha.inserir(linha)
            fila.inserir(linha)

def adicao_remocao(hashtable, pilha, fila):
    with open("./operacoes.txt", "r") as arq:
        operacoes = []
        for linha in arq:
            dados = linha.strip().split('\t')
            operacoes.append(dados)
        
        # Hash Table
        for i in range(len(operacoes)):
            if len(operacoes[i]) == 3:
                posicao, operacao, valor = operacoes[i]
                print(f"h\t{operacao}\t", hashtable.inserir_posicao(int(posicao), valor))
            else:
                posicao, operacao = operacoes[i]
                print(f"h\t{operacao}\t", hashtable.remover_posicao(int(posicao)))

        # Pilha
        for i in range(len(operacoes)):
            if len(operacoes[i]) == 3:
                posicao, operacao, valor = operacoes[i]
                print(f"p\t{operacao}\t", pilha.inserir_posicao(int(posicao), valor))
            else:
                posicao, operacao = operacoes[i]
                print(f"p\t{operacao}\t", pilha.remover_posicao(int(posicao)))

        # Fila
        for i in range(len(operacoes)):
            if len(operacoes[i]) == 3:
                posicao, operacao, valor = operacoes[i]
                print(f"f\t{operacao}\t", fila.inserir_posicao(int(posicao), valor))
            else:
                posicao, operacao = operacoes[i]
                print(f"f\t{operacao}\t", fila.remover_posicao(int(posicao)))


hashtable = Hashtable()
pilha = Pilha()
fila = Fila()
ler_arquivo(hashtable, pilha, fila)
print(f"Posição 1, memória, tempo      -> Hashtable: {hashtable.valor_posicao(1)}, Pilha: {pilha.valor_posicao(1)}, Fila: {fila.valor_posicao(1)}")
print(f"Posição 100, memória, tempo    -> Hashtable: {hashtable.valor_posicao(100)}, Pilha: {pilha.valor_posicao(100)}, Fila: {fila.valor_posicao(100)}")
print(f"Posição 1000, memória, tempo   -> Hashtable: {hashtable.valor_posicao(1000)}, Pilha: {pilha.valor_posicao(1000)}, Fila: {fila.valor_posicao(1000)}")
print(f"Posição 5000, memória, tempo   -> Hashtable: {hashtable.valor_posicao(5000)}, Pilha: {pilha.valor_posicao(5000)}, Fila: {fila.valor_posicao(5000)}")
print(f"Última Posição, memória, tempo -> Hashtable: {hashtable.valor_posicao(hashtable.tamanho()-1)}, Pilha: {pilha.valor_posicao(pilha.tamanho()-1)}, Fila: {fila.valor_posicao(fila.tamanho()-1)}")
#adicao_remocao(hashtable, pilha, fila)