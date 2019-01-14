# -*-coding:utf-8-*-
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.142.10', 8080))

while True:
    data = input('请输入给服务器发送的数据:')
    client.send(data.encode())
    info = client.recv(1024)
    print('服务器说:', info.decode('utf-8'))