import socket

def enviar_mensagem(endereco, porta):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mensagem = "Mensagem enviada de cliente UDP"
    client_socket.sendto(mensagem.encode(), (endereco, porta))
    resposta, _ = client_socket.recvfrom(1024)
    print(f"Resposta do servidor: {resposta.decode()}")
    client_socket.close()

endereco = "localhost"
porta = 1224
enviar_mensagem(endereco, porta)
