import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg='KEEPALIVE\nname dongliang\n'
s.sendto(msg, address)

s.close()
