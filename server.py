import socket
host = "127.0.0.1"
port=10000
server=socket.socket()
server.bind((host,port))
server.listen()
conn, addr = server.accept()
while True:
    x=conn.recv(1024)
    x=x.decode()
    print(x)
    y=input('Enter data :- ')
    data = y.encode()
    conn.send(data)
    if (y=='Close'):
        break
server.close()
