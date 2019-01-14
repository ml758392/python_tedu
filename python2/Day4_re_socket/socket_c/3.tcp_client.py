import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.142.1', 8080))


while True:
    data = input('发给服务器的信息:').encode()
    client.send(data)
    info = client.recv(1024)
    print('服务器说：', info.decode('utf-8'))