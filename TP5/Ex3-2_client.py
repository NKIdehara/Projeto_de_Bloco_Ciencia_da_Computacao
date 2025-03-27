import socket
import ssl

HOST = 'localhost'
PORT = 4443

contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
contexto.load_verify_locations("server.crt")
contexto.check_hostname = False

with socket.create_connection((HOST, PORT)) as conexao:
    with contexto.wrap_socket(conexao, server_hostname=HOST) as tls_cliente:
        def interceptando_enviados(dados):
            print(f"Interceptado enviados: {dados.decode()}")
            return dados_enviados(dados)
        def interceptando_recebidos(buffer):
            dados = dados_recebidos(buffer)
            if dados:
                print(f"Interceptado recebidos: {dados.decode()}")
            return dados
        dados_enviados = tls_cliente.sendall
        tls_cliente.sendall = interceptando_enviados
        dados_recebidos = tls_cliente.recv
        tls_cliente.recv = interceptando_recebidos

        # original Ex3-1_client.py
        print("Conectado ao servidor TLS")
        mensagem = "Teste de conexão."
        tls_cliente.sendall(mensagem.encode())
        dados = tls_cliente.recv(1024)
        print(f"Resposta do servidor: {dados.decode()}")
