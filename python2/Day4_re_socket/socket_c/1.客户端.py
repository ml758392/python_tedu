import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('www.baidu.com', 80))


client.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

data = []
while True:
    temdata = client.recv(1024)
    if temdata:
        data.append(temdata)
    else:
        break

datastr = (b''.join(data)).decode('utf-8')

client.close()

# print(datastr)
headers, Html = datastr.split('<html>', 1)
print(headers)
print('*'*50)
print(Html)