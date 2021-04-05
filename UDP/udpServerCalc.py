import socket

def Main():

	host = '127.0.0.1'
	port = 4444

	# Create UDP Socket Server (Network,Transport)
	socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Configure IP Address Server and Port will be running
	socketUDP.bind((host,port))

	print('UDP Server: {}:{}'.format(host,port))

	while(True):
		print('Waiting messages...')
		operation,address = socketUDP.recvfrom(4096) # Buffer size - bytes

		print('Received {} bytes from {}'.format(len(operation), address))
		print(operation)

		if (operation):
			try:
				# Conversion from Bytes to String
				operation = operation.decode()

				# Function that allows Python code execution inside you
				result = eval(operation)

				deliver = operation + ' = ' + str(result)

				# Conversion from String to Bytes
				deliver = str(deliver).encode()
				send = socketUDP.sendto(deliver, address)

			except (RuntimeError, TypeError, NameError, SyntaxError):
				deliver = str('Error').encode()
				send = socketUDP.sendto(deliver, address)

		else:
			break

	socketUDP.close()


if __name__ == '__main__':
	Main()
