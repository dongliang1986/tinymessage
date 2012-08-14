import socket
sockTable={}
def receiveHandler(data, addr):
    handlerDict={'KEEPALIVE': receiveKLHandler}
    lines = data.split('\n')
    handlerDict[lines[0]](lines[1:], addr)
def receiveKLHandler(lines, addr):
    line = lines[0]
    type,value = tuple(line.split())
    if type != 'name':
        sys.stderr.write('invalid option')
        return
    sockTable[addr] = value
    pass
if __name__ == '__main__':
    address = ('127.0.0.1', 31500)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(address)

        
    while True:
        data, addr = s.recvfrom(2048)
        if not data:
            print "client has exist"
            break
        print "received:", data, "from", addr
        receiveHandler(data, addr)
    s.close()
