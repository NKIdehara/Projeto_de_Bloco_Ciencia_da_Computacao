import dns.resolver

dominio = "infnet.edu.br"
tipos = ["A", "MX", "NS"]
for tipo in tipos:
    print(f"\n'{tipo}' de {dominio}")
    respostas = dns.resolver.resolve(dominio, tipo)
    for resposta in respostas:
        if tipo == "MX":
            print(f"Prioridade: {resposta.preference}, Servidor: {resposta.exchange}")
        else:
            print(resposta.to_text())
