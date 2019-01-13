# -*-coding:utf-8-*-
import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(('10.0.142.206', 2425))
udp.sendto('sunck is a nice man'encode())
while True:
    udp.send('sunck is  good man'.encode())
    time.sleep(1)