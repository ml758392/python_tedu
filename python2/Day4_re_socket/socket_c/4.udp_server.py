import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('192.168.142.1', 8080))

while True:
    data, addr = server.recvfrom(1024)
    print('客户端说:', data.decode('utf-8'))
    info = input('请输入数据：')
    server.sendto(info.encode(), addr)