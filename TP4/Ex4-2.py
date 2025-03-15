import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 1224))

msg = "Mensagem enviada de cliente TCP"
client_socket.sendall(msg.encode())
print(f'Mensagem enviada: {msg}')

msg = client_socket.recv(1024)
print("Mensagem do servidor:", msg.decode())
client_socket.close()
