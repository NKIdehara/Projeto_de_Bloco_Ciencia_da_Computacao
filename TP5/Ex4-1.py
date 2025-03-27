from scapy.all import ARP, sr

intervalo = "192.168.1.1/24"
pacote = ARP(pdst=intervalo)
resposta, _ = sr(pacote, timeout=10, verbose=False)
print("Hosts na rede:")
for enviado, recebido in resposta:
    print(f"IP: {recebido.psrc}\tMAC: {recebido.hwsrc}")
