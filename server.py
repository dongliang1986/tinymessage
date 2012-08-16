import socket
class LoginInfo:
    '''用户登录信息
'''
    def __init__(self):
        self.sockTable={} #地址<->用户名
        self.userTable={} #用户名<->地址
    def insert(self, addr, user):
        if self.sockTable.has_key(addr):
            self.userTable.pop(self.sockTable[addr])
        self.sockTable[addr] = user
        self.userTable[user] = addr
loginInfo = LoginInfo()
def receiveHandler(data, addr):
    '''收包处理
'''
    handlerDict={'KEEPALIVE': receiveKLHandler,
                 'MESSAGE' : receiveMSGHandler}
    lineGen = (i for i in data.split('\n') if len(i) != 0)
    line = lineGen.next()
    handlerDict[line](lineGen, addr)
    
def receiveKLHandler(lineGen, addr):
    line = lineGen.next()
    loginInfo.insert(addr, line)
def receiveMSGHandler(lineGen, addr):
    receiver = lineGen.next()
    sendMSG(receiver, lineGen)
def sendMSG(receiver, lineGen):
    message = [ i for i in lineGen]
    message = '\n'.join(message)
    
    print receiver, message
s = None  
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
