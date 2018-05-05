import socket

# HOST = "172.16.73.1"
HOST = "::172.16.73.1"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
# tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSock.connect(ADDR)
while True:
    msg = input("msg> ")
    if msg == "exit":
        break
    tcpSock.send(msg.encode('utf-8'))    
    recv = tcpSock.recv(BUFSIZ).decode('utf-8')
    print(recv)
tcpSock.close()