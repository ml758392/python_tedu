# -*-coding:utf-8-*-
import socket


udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpserver.bind