import socket
host = "127.0.0.1"
port = 10000
print('Connecting to servers......')
cs = socket.socket()
print('........wait for it USER.........')
cs.connect((host,port))
print('Connection established to Vandan\'s server!\nWelcome to Vandan SERVER')
while True:
    x = input('Enter message to be sent :')
    y = x.encode()
    cs.send(y)
    data = (cs.recv(1024)).decode()
    if(data == 'Close'):
        break
    print(data)
print('Server is closed')
cs.close()
