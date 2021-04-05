import socket, threading, sys

connections = []

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
            
    connection.close()
    
def startThread(connection):
    while True:
        print('Waiting for messages...')
        # Receive message from client
        data = connection.recv(1024) # Buffer size - bytes

        if data:
            message = data.decode().split('|')[1].casefold()
        
        if not data or message == 'q':
            removeConnection(connection)
            break

        print('Received {} bytes from {}'.format(len(data), connection.getpeername()))

        # Returns the message to all clients
        broadcast(connection, dataFormatting(data))

def broadcast(connection, data):
    # Send message to all clients
    for c in connections:
        if c != connection:
            c.send(data)

def removeConnection(connection):
    # Remove and close connection from the connections list
    for c in connections:
        if c == connection:
            connections.remove(c)
            c.close()

def dataFormatting(data):
    # Separating data into variables
    data = data.decode().split('|')
    name = data[0]
    message = data[1]
    colorNumber = data[2]
    openColor = '\033[{}m'.format(colorNumber)
    closeColor = '\033[0m'
    
    # Formatting data
    if message != 'left' and message != 'joined':
        data = '{}{}: {}{}'.format(openColor, name, closeColor, message)
        data = data.encode()

    elif message:
        data = '{}{} {}{}'.format(openColor, name, message, closeColor)
        data = data.encode()

    return data

if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(e)
