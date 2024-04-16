import socket
host = "127.0.0.1"
port = 10000
server = socket.socket()
server.bind((host,port))
server.listen()
conn, addr = server.accept()
print('Connection Established with Vandan!')
while True:
    x = conn.recv(1024)
    x.decode()
    print(x)
    y = input('Enter Data :')
    data = y.encode()
    conn.send(data)
    if(y=='Close'):
        break
server.close()
