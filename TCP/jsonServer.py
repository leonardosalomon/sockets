import socket, json

class Message(object):
    def __init__(self):
        self.user = ''
        self.message = ''

def Main():
    host = '0.0.0.0'
    port = 2424

    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketTCP.bind((host,port))
    socketTCP.listen(1)

    print('TCP Server: {}:{}'.format(host,port))

    connection, address = socketTCP.accept()
    print('Connected: ' + str(address))

    # Receive client message
    data = connection.recv(4096)

    # Print serialized message
    print(data)

    # Desserializes the received message, making the object available again in memory
    receivedObject = json.loads(data)

    # Print data object
    print(receivedObject.get('user'))
    print(receivedObject.get('message'))

    connection.close()

if __name__ == '__main__':
    Main()
