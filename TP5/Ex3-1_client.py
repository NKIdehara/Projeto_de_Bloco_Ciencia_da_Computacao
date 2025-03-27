import socket
import ssl

HOST = 'localhost'
PORT = 4443

contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
contexto.load_verify_locations("server.crt")
contexto.check_hostname = False

with socket.create_connection((HOST, PORT)) as conexao:
    with contexto.wrap_socket(conexao, server_hostname=HOST) as tls_cliente:
        print("Conectado ao servidor TLS")
        mensagem = "Teste de conexão."
        tls_cliente.sendall(mensagem.encode())
        dados = tls_cliente.recv(1024)
        print(f"Resposta do servidor: {dados.decode()}")
