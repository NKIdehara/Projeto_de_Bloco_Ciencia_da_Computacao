import socket

def iniciar_servidor(endereco, porta):
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_servidor.bind((endereco, porta))
    print(f"Servidor UDP {endereco}:{porta}")
    print("Aguardando mensagens...\n")
    while True:
        mensagem, endereco = socket_servidor.recvfrom(1024)
        print(f"Mensagem recebida de {endereco}: {mensagem.decode()}")
        resposta = "ack"
        socket_servidor.sendto(resposta.encode(), endereco)

endereco = "0.0.0.0"
porta = 1224
iniciar_servidor(endereco, porta)
