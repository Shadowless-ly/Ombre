import socket
import sys

HOST = "172.16.73.1"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udp_client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

while True:
    data = input("> ")
    if not data:
        break
    udp_client_sock.sendto(data.encode('utf-8'), ADDR)
    data, addr = udp_client_sock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
udp_client_sock.close()