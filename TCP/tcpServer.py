import socket

def Main():

	host = '0.0.0.0'
	port = 6868

	# Cria o socket TCP do servidor (Internet, Transporte)
	socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Configura o IP e a porta que o servidor vai ficar executando
	socketTCP.bind((host,port))

	print('Servidor TCP: {}:{}'.format(host,port))

	# Habilita o servidor para aceitar conexões
	# O parâmetro indica a quantidade máxia de solicitações de conexão qque podem ser enfileiradas, antes de serem recusadas. Ex: 5 (congestionamento)
	socketTCP.listen(1)

	# Fica bloqueado aguardando a conexão de um cliente
	conn, addr = socketTCP.accept()

	print('Conexão realizada por: ' + str(addr))

	while True:
		print('Esperando mensagens...')
		data = conn.recv(1024) # buffer size - bytes

		if not data:
			break

		print('Recebido {} bytes de {}'.format(len(data), conn.getpeername()))


		# Devolve a mensagem para o cliente
		conn.send(data.upper())

	conn.close()

if __name__ == '__main__':
	Main()
