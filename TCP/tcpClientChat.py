import socket, threading, time
from random import randrange

def Main():
    host = '127.0.0.1'
    port = 6868
    global mySocket
    # Create socket Client
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connection with the server
    mySocket.connect((host,port))

    randomNumber = str(randrange(90,96))

    # Creation of the message receiving thread
    thread = threading.Thread(target=startThread, args=[mySocket])
    thread.start()

    print('\nq = Quit')
    name = input('\nEnter your name: ')


    while name == '':
        name = input('Enter your name: ')

    if name.casefold() == 'q' or name == '':
        message = 'q'
        name = 'Anonymous'
        msg = 'joined'
        # Sends the user's message to the server
        sendData(mySocket, name, msg, randomNumber)
    else:
        msg = 'joined'
        # Sends the user's message to the server
        sendData(mySocket, name, msg, randomNumber)
        
        print('\n\033[44mWelcome to Chat!!!\033[0m\n')
    
        print('q = Quit\n')

        # Waits for the user to type a message
        message = input('Enter your message: ')
    while True:
        if message.casefold() == 'q':
            msg = 'left'
            # Sends the user's message to the server
            sendData(mySocket, name, msg, randomNumber)
            sendData(mySocket, name, message, randomNumber)
            break
        elif message == '':
            message = input('')
        else:
            # Sends the user's message to the server
            sendData(mySocket, name, message, randomNumber)
            # Awaits new user message
            message = input('')
    mySocket.close()

def startThread(clientSocket):
    while True:
        # Receives the message bounce from the server
        data = clientSocket.recv(1024) # Buffer size - Bytes
        if data:
            print(data.decode())
        else:
            break

def sendData(mySocket, name, message, randomNumber):
    # Send data to the server
    data = name + '|' + message + '|' + randomNumber
    mySocket.send(data.encode())
    time.sleep(0.01)

if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        sendData(mySocket, '', 'q', '')
        mySocket.close()
    except ConnectionRefusedError:
        print('The server is not running')
    except Exception as e:
        print(e)
