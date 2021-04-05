import socket 

def Main():

	# Create Client Socket
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Define the server address and port
	destiny = ('127.0.0.1', 4444)

	# Start message
	print('\n\33[44m SOCKET UDP CALCULATOR PYTHON \33[0m')

	# Wait for the user to enter the operation
	operation = input('\nAddition = + \nSubtraction = - \nMultiplication = * \nDivision = / \nModule = %\nQuit = q \n\n(Operation Example: 10*3) \n\nType the math operation: ')

	while operation != 'q' and operation:

		# Sends client operation to the server
		sends = clientSocket.sendto(operation.encode(), destiny)

		# Receive server response
		response, server = clientSocket.recvfrom(4096)
		
		if(response.decode() == 'Error'):
			print('\33[41m' + '\nResponse received from the server \n{}: {} '.format(server, response.decode()) + '\nPlease contact system administrator \33[0m')
		else:
			print('\33[42m' + '\nResponse received from the server {}: {} \33[0m'.format(server, response.decode()))

		operation = input('\nAddition = + \nSubtraction = - \nMultiplication = * \nDivision = / \nModule = %\nQuit = q \n\n(Operation Example: 10*3) \n\nType the math operation: ')

	clientSocket.close()


if __name__ == '__main__':
	Main()
