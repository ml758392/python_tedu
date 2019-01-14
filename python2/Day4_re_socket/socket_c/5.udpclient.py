import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    info = input('发给服务器的数据:').encode()
    client.sendto(info,('192.168.142.1', 8080))
    data = client.recv(1024)
    print(data.decode('utf8'))
