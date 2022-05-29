import socket
from time import sleep
from Record import RecordUDP

# MAX_DGRAM = 2**16
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('0.0.0.0', 20001))

# while True:
#     seg, addr = s.recvfrom(MAX_DGRAM)
#     print(addr)

rec_udp = RecordUDP()
rec_udp.start()