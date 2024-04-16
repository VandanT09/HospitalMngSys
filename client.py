import socket
host="127.0.0.1"
port=10000
cs=socket.socket()
cs.connect((host,port))
while True:
    x=input('Enter message to sent :-')
    y=x.encode()
    cs.send(y)
    data=(cs.recv(1024)).decode()
    if(data=='Close'):
        break
    print(data)
cs.close()
