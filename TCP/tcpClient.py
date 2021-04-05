import socket

def Main():
    
    host = '127.0.0.1'
    port = 6868

    # Cria o socket do cliente
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Realiza a conexão com o servidor
    mySocket.connect((host,port))

    # Aguarda o usuário a digitar uma mensagem
    message = input(' -> (q sair) ')

    while message != 'q' and message:
        # Envia a mensagem do suuário para o servidor
        mySocket.send(message.encode())

        # Recebe a devolução da mensagem do servidor
        data = mySocket.recv(1024) # buffer size - bytes

        print('Recebido do servidor {}: {}'.format(mySocket.getpeername(), data.decode()))

        # Aguarda nova mensagem do usuário
        message = input(' -> (q sair) ')

    mySocket.close()

if __name__ == '__main__':
    Main()
