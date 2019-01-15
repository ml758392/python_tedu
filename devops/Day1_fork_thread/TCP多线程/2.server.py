# -*-coding:utf-8-*-
import socket
import threading

# 创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP端口
server.bind(('192.168.142.10', 8080))

# 监听
server.listen(5)
print('服务器启动成功.....')


def run(clientsocket):
    print('%s 连接成功' % (str(clientsocket)))
    data = clientsocket.recv(1024)
    print('收到client的数据：' + data.decode('utf-8'))
    clientsocket.send(data)


while True:
    # 等待连接
    clientsocket, clientaddress = server.accept()
    t = threading.Thread(target=run, args=(clientsocket,))
    t.start()


