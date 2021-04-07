import socket, threading, time, pickle, os, sys
from random import randrange
from tkinter import filedialog
from tkinter import Tk

# Data object
class data(object):
    def __init__(self):
        self.name = ''
        self.message = ''
        self.file = ''
        self.filename = ''
        self.randomNumber = str(randrange(90,96))

def Main():
    host = '127.0.0.1'
    port = 6868
    global mySocket
    # Create socket Client
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('\nq = Quit')
    global client
    client = data()
    client.name = input('\nEnter your name: ')

    # Loop until the client informs the name
    while client.name == '':
        client.name = input('Enter your name: ')

    # If the user wants to leave when entering the name
    if client.name.casefold() == 'q':
        sys.exit()

    if client.name:
        # Connection with the server
        mySocket.connect((host,port))
        # Creation of the message receiving thread
        thread = threading.Thread(target=startThread, args=[mySocket])
        thread.start()
        # User joins the conversation
        client.name = client.name.title()
        client.message = 'joined'
        sendData(mySocket, client)
        
        print('\n\033[1m\033[34mWelcome to Chat!!!\033[0m\n')
    
        print('q = Quit')
        print('f = Send file\n')

        # Waits for the client to type a message
        client.message = input('Enter your message: ')
        
    while True:
        # If message is q client leaves the chat
        if client.message.casefold() == 'q':
            client.message = 'left'
            sendData(mySocket, client)
            client.message = 'q'
            sendData(mySocket, client)
            break
        # If message is f client send file
        elif client.message.casefold() == 'f':
            # Open a window for the client to choose the file
            root = Tk()
            root.withdraw()
            filePath = filedialog.askopenfilename(initialdir = "/",title = "Choose a file",filetypes = (("all files","*.*"),("all files","*.*")))
            if filePath:
                # Open file in read mode to read the bytes and save them
                file = open(filePath, 'rb')
                client.file = file.read()
                client.filename = os.path.basename(filePath)
                sendData(mySocket, client)
                client.file = ''
                client.message = input('')
            else:
                client.message = input('')
        # Force to have content in the message 
        elif client.message == '':
            client.message = input('')
        else:
            sendData(mySocket, client)
            # Awaits new client message
            client.message = input('')
    mySocket.close()

def startThread(clientSocket):
    while True:
        # Receives the message bounce from the server
        receivedData = clientSocket.recv(10*1024) # Buffer size - Bytes
        if receivedData:
            # Desserializes the received message
            receivedData = pickle.loads(receivedData)
            # If the message is object of type data
            if type(receivedData) == type(data()):
                # Creating an empty file with the object's file name, opening it in write mode to save the data, and then closing it
                file = open(receivedData.filename, 'wb')
                file.write(receivedData.file)
                file.close()
            else:
                print(receivedData)
        else:
            break

def sendData(mySocket, object):
    # Send serialized data to the server
    data = pickle.dumps(object)
    mySocket.send(data)
    time.sleep(0.01)

if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        if client.name:
            client.message = 'left'
            sendData(mySocket, client)
            client.message = 'q'
            sendData(mySocket, client)
            mySocket.close()
        else:
            sys.exit()
    except ConnectionRefusedError:
        print('The server is not running')
    except Exception as e:
        print(e)
