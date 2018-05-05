import socket
import time

HOST = "172.16.73.1"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udp_server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_sock.bind(ADDR)

while True:
    print("waiting for message...")
    data, addr = udp_server_sock.recvfrom(1024)
    data = '[%s] %s' %(time.ctime(), data.decode('utf-8'))
    udp_server_sock.sendto(data.encode('utf-8'), addr)
    print('...received from and returned to:', addr)
udp_server_sock.close()