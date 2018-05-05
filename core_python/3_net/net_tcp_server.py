import socket
import time
import sys

# HOST = "172.16.73.1"
HOST = "::172.16.73.1"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
# tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
tcp_sock.bind(ADDR)
tcp_sock.listen(5)
try:
    while True:
        print("waiting for connection...")
        tcp_clisock, addr = tcp_sock.accept()
        print("...connected from:", addr)
        while True:
            data = tcp_clisock.recv(BUFSIZ)
            if not data:
                break
            msg = "[%s] %s" % (time.ctime(), data.decode('utf-8'))
            tcp_clisock.send(msg.encode('utf-8'))
        tcp_clisock.close()
except KeyboardInterrupt as e:
    tcp_sock.close()
    sys.exit(0)


# udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
