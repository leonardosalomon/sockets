import socket
from tkinter import filedialog
from tkinter import Tk

#abre uma tela para escolha do arquivo
root = Tk()
root.withdraw()
filePath = filedialog.askopenfilename(initialdir = "/",title = "Escolha um arquivo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print(filePath)
    
# File to send
# filePath = 'fileServe.py'

# Create socket
serverSocket = socket.socket()
serverSocket.bind(('localhost', 5252))
serverSocket.listen(5)

# Wait new clients

# When receiving the connection from a new client, send the file to him
while True:
    clientSocket, address = serverSocket.accept()
    # Open the file and sends it to the client in parts
    with open (filePath, 'rb') as f:
        clientSocket.sendfile(f, 0)
    # Close client socket
    clientSocket.close()
