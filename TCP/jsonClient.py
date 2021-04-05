import socket, json

class Message(object):
    def __init__(self):
        self.user = ''
        self.message = ''

def Main():
    host = '127.0.0.1'
    port = 2424

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.connect((host, port))

    # Create object
    objectSend = Message()
    objectSend.user = input('Enter your name: ')
    objectSend.message = input('Enter your message: ')

    # Object serialization
    # __dict__ is an attribute of keeping instance attributes on objects
    data = json.dumps(objectSend.__dict__) # , indent=4 for indentation


    print(data)

    # Send serialized object to the server
    mySocket.send(data.encode())

    mySocket.close()

if __name__ == '__main__':
    Main()
