import ipaddress
import random
import time

class No_Trie:
    def __init__(self):
        self.filhos = {}
        self.prefixo = None

class Trie:
    def __init__(self):
        self.raiz = No_Trie()

    def inserir(self, prefixo):
        network = ipaddress.ip_network(prefixo, strict=False)
        octetos = str(network.network_address).split('.')[:network.prefixlen // 8]
        no = self.raiz
        for octeto in octetos:
            if octeto not in no.filhos:
                no.filhos[octeto] = No_Trie()
            no = no.filhos[octeto]
        no.prefixo = prefixo

    def maior_prefixo_encontrado_trie(self, ip):
        octetos = str(ipaddress.ip_address(ip)).split('.')
        no = self.raiz
        maior_encontrado = None
        for octeto in octetos:
            if octeto in no.filhos:
                no = no.filhos[octeto]
                if no.prefixo:
                    maior_encontrado = no.prefixo
            else:
                break
        return maior_encontrado

def maior_prefixo_encontrado_linear(ip, prefixos):
    encontrado = None
    tam_encontrado = -1
    endereco = ipaddress.ip_address(ip)
    for prefixo in prefixos:
        network = ipaddress.ip_network(prefixo, strict=False)
        if endereco in network:
            if network.prefixlen > tam_encontrado:
                encontrado = prefixo
                tam_encontrado = network.prefixlen
    return encontrado

def prefixos_aleatorios(qtde):
    prefixos = []
    for _ in range(qtde):
        ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0"
        tamanho_prefixo = random.randint(8, 32)
        prefixos.append(f"{ip}/{tamanho_prefixo}")
    return prefixos

prefixos = prefixos_aleatorios(100_000)
prefixos.append("192.168.1.0/24")
ip = "192.168.1.55"

t_ini = time.time()
resultado = maior_prefixo_encontrado_linear(ip, prefixos)
t_fim = time.time()
print(f"Linear\t{ip}: {resultado}, Tempo: {(t_fim - t_ini):.2f}")

trie = Trie()
for prefixo in prefixos:
    trie.inserir(prefixo)
t_ini = time.time()
resultado = trie.maior_prefixo_encontrado_trie(ip)
t_fim = time.time() 
print(f"Trie\t{ip}: {resultado}, Tempo: {(t_fim - t_ini):.2f}")