from time import sleep
from PiRecord import Capture
import socket
import base64

cap_ = Capture(width=1920, height=1080, fps=50)
BUFF_SIZE = 65536
# Create a UDP socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = '192.168.2.41'
print(host_ip)
port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)
print('Listening at:', socket_address)
while True:
    msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
    print('GOT connection from ', client_addr)
    cap_.start()
    while True:
        if cap_.ret():
            yuv420 = cap_.read()
            message = base64.b64encode(yuv420)
            server_socket.sendto(message, client_addr)
server_socket.close()