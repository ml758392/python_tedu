# -*-coding:utf-8-*-
import socket


udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpserver.bind(('192.168.142.10', 8900))

while True:
    data, addr = udpserver.recvfrom(1024)
    print('客户端说:', data.decode('utf-8'))
    info = input("请输入数据：")
    udpserver.sendto(info.encode(), addr)
