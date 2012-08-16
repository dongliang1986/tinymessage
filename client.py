import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg='KEEPALIVE\ndongliang\n'
s.sendto(msg, address)
msg='MESSAGE\ndongliang\nhello\nworld\n'
s.sendto(msg, address)

s.close()
