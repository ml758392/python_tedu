# -*-coding:utf-8-*-
import urllib.request
import urllib.parse

url = 'http://www.sunck.wang:8085/form'
# 将要发送的数据合成一个字典
# 字典的健取网址里找，一般为input标签的name属性的值
data = {
    'username': 'sunck',
    'passwd': "666"
}

# 对要发送的数据进行打包，记住编码
postData = urllib.parse.urlencode(data).encode('utf-8')

# 请求体
req = urllib.request.Request(url, data=postData)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/60.0.3112.113 Safari/537.36')
response = urllib.request.Request(req)
print(response.data().decode('utf-8'))
