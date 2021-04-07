import socket, threading, sys, pickle, time

connections = []

# Data object
class data(object):
    def __init__(self):
        self.name = ''
        self.message = ''
        self.file = ''
        self.filename = ''
        self.randomNumber = ''

def Main():

    host = '0.0.0.0'
    port = 6868
    
    # Create socket TCP of the Server (Internet, Transport)
    socketTCPServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Configures the IP and the port that the server will be running
    socketTCPServer.bind((host,port))
    
    print('TCP Server: {}:{}'.format(host,port))

    # Enables the server to accept connections
    # The parameter indicates the maximum number of connection requests that can be queued, before being refused. Ex: 5 (congestion)
    socketTCPServer.listen(1)
    
    while True:
        # It is blocked waiting for a client to connect
        connection, address = socketTCPServer.accept()
        # Add connection in connections list
        connections.append(connection)
        # Limiting number of connections
        # if len(connections) > 2: 
        #     connections.remove(connection)
        #     connection.close()
        # else:
        print('Connected: ' + str(address))
        
        # Creates and triggers the execution of the client thread
        thread = threading.Thread(target=startThread, args=[connection])
        thread.start()
            
def startThread(connection):
    while True:
        print('Waiting for messages...')
        # Receive message from client
        data = connection.recv(10*1024) # Buffer size - bytes
        global receivedObject
        
        if data:
            # Desserializes the received message, making the object available again in memory   
            receivedObject = pickle.loads(data)

        # If there is no data or if the client sends q closes and removes the connection from the list
        if not data or receivedObject.message == 'q':
            removeConnection(connection)
            break

        print('Received {} bytes from {}'.format(len(data), connection.getpeername()))

        # If there is a file in the object, send it to all clients
        if receivedObject.file:
            broadcast(connection, pickle.dumps(receivedObject))
            time.sleep(0.01)
        # Returns the message to all clients
        broadcast(connection, dataFormatting(receivedObject))

def broadcast(connection, object):
    # Scrolls through the connections array sending the message to everyone connected with the exception of who sent it
    for c in connections:
        if c != connection:
            c.send(object)

def removeConnection(connection):
    # Traverses the connection array by removing the desired connection from the array and closing the socket
    for c in connections:
        if c == connection:
            connections.remove(c)
            c.close()

def dataFormatting(object):
    # Variable name colors
    openColor = '\033[1m\033[{}m'.format(object.randomNumber)
    closeColor = '\033[0m'
    openColorFile = '\033[1m\033[32mReceived File = '
    # Formatting data and serializing
    # If message text normal
    if object.message != 'left' and object.message != 'joined' and object.message != 'f':
        data = '{}{}{}: {}'.format(openColor, object.name, closeColor, object.message)
        data = pickle.dumps(data)
    # If file message 
    elif object.message == 'f':
        data = '{}{}{}: {}'.format(openColor, object.name, closeColor, openColorFile + object.filename + closeColor)
        data = pickle.dumps(data)
    # If login or logout
    elif object.message:
        data = '{}{} {}{}'.format(openColor, object.name, object.message, closeColor)
        data = pickle.dumps(data)

    return data

if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(e)
