import ipaddress

def ip_dentro(ip, prefixo):
    rede = ipaddress.ip_network(prefixo)
    endereco = ipaddress.ip_address(ip)
    return endereco in rede.hosts()

ip = "192.168.1.5"
prefixo = "192.168.1.0/24"
print(f"IP {ip} está dentro do prefixo {prefixo}: {ip_dentro(ip, prefixo)}")

ip = "192.168.1.5"
prefixo = "192.168.2.0/29"
print(f"IP {ip} está dentro do prefixo {prefixo}: {ip_dentro(ip, prefixo)}")
