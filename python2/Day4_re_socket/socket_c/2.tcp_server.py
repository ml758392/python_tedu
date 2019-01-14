import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('192.168.142.1', 8080))

server.listen(5)

print('服务器启动成功.......')

csocket, caddr = server.accept()

print('%s链接成功' % str(csocket))

while True:
    data = csocket.recv(1024)
    print('收到client的数据：'+data.decode('utf-8'))
    csocket.send((data))
