# -*-coding:utf-8-*-
import socket

# 1.创建一个socket
# 参数1：指定协议 AF_INET  或者 AF_INET6
# 参数2：SOCK_STREAM执行使用面向流的TCP协议

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.建立连接
# 参数：是一个元组，第一个元素为要连接的服务器的IP地址，第二个参数为端口
sk.connect(('www.sina.com.cn', 80))
sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 等待接受数据
data = []
while True:
    #  每次接受1K的数据
    tempdata = sk.recv(1024)
    if tempdata:
        data.append(tempdata)
    else:
        break

datastr = (b''.join(data)).decode('utf-8')


# 断开连接
sk.close()
# print(datastr)

headers, HTML = datastr.split('\r\n\r\n', 1)
print(headers)
print('#'*50)
print(HTML)
