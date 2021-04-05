import socket

# Create socket and connect to the server
socket = socket.socket()
socket.connect(('localhost',5252))

# Buffer size
bufferSize = 8 * 1024

# Create a new empty file to receive the uploaded file 
file = open('fileReceived.png', 'wb')

# Receive the first bytes of the file
chunk = socket.recv(bufferSize)

# Stay in loop receiving the other parts of the file
while chunk:
    # Write the bytes received in the file
    file.write(chunk)
    # Await the sending of new bytes 
    chunk = socket.recv(bufferSize)

# Close file
file.close()

# Close socket
socket.close()
