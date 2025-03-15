import socket

def iniciar_servidor(endereco, porta):
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind((endereco, porta))
    socket_servidor.listen(1)
    print(f"Servidor TCP {endereco}:{porta}")
    print("Aguardando conexão...\n")
    while True:
        socket_cliente, endereco_cliente = socket_servidor.accept()
        print(f"Conexão recebida de {endereco_cliente}")
        socket_cliente.send(b"Seja bem vindo!\n")
        socket_cliente.close()

endereco = "0.0.0.0"
porta = 1224
iniciar_servidor(endereco, porta)
