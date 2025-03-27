import socket
import ssl

HOST = '0.0.0.0'
PORT = 4443

contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
contexto.load_cert_chain(certfile="server.crt", keyfile="server.key")

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen(5)

print(f"Servidor TLS rodando em {HOST}:{PORT}")

while True:
    conexao, endereco = servidor.accept()
    with contexto.wrap_socket(conexao, server_side=True) as tls_servidor:
        print(f"Conexão segura estabelecida com {endereco}")
        while True:
            dados = tls_servidor.recv(1024)
            if not dados:
                break
            print(f"Recebido: {dados.decode()}")
            tls_servidor.sendall(dados)
