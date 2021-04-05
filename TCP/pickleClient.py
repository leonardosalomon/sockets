import socket, pickle

class Message(object):
    def __init__(self):
        self.user = ''
        self.message = ''

def Main():
    host = '127.0.0.1'
    port = 3232

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.connect((host, port))

    # Create object
    objectSend = Message()
    objectSend.user = input('Enter your name: ')
    objectSend.message = input('Enter your message: ')

    # Object serialization
    data = pickle.dumps(objectSend)

    # Send serialized object to the server
    mySocket.send(data)

    mySocket.close()

if __name__ == '__main__':
    Main()
