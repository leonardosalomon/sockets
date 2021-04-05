import socket

def Main():

	# Cria o socket do cliente
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Define o endereço e porta do servidor
	destino = ('127.0.0.1', 7777)

	# Aguarda o usuário digitar uma mensagem
	message = input(' -> (q sair) ')
	
	while message != 'q' and message:
		# Envia a mensagem do usuário para o servidor
		sent = mySocket.sendto(message.encode(), destino)

		# Recebe a devolução da mensagem do servidor
		data, server = mySocket.recvfrom(4096)
		
		print('Recebido do servidor {}: {}'.format(server,data.decode()))

		# Aguarda nova mensagem do usuário
		message = input(' -> (q sair)')
		
	mySocket.close()

if __name__ == '__main__':
	Main()
