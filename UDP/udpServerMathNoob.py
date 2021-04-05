import socket

def Main():

	host = '127.0.0.1'
	port = 4444

	# Cria o socket UDP do servidor (Internet,Transporte)
	socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Configura o IP e a porta que o servidor vai ficar executando
	socketUDP.bind((host,port))

	print('Servidor UDP: {}:{}'.format(host,port))

	while(True):
		print('Esperando mensagens...')
		data,address = socketUDP.recvfrom(4096) # Buffer size - bytes

		print('Recebido {} bytes de {}'.format(len(data), address))
		print(data)

		if (data):
			sent = socketUDP.sendto(mathOperation(data), address)
		else:
			break

	socketUDP.close()

def mathOperation (var):
	vard = var.decode()

	if vard.find('+') > 0:
		vard = float(vard.split('+')[0]) + float(vard.split('+')[1])
	elif vard.find('-') > 0:
		vard = float(vard.split('-')[0]) - float(vard.split('-')[1])
	elif vard.find('*') > 0:
		vard = float(vard.split('*')[0]) * float(vard.split('*')[1])
	elif vard.find('/') > 0:
		vard = float(vard.split('/')[0]) / float(vard.split('/')[1])
	elif vard.find('%') > 0:
		vard = float(vard.split('%')[0]) % float(vard.split('%')[1])

	return str(vard).encode()

if __name__ == '__main__':
	Main()
