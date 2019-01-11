# -*-coding:utf-8-*-
import urllib.request
url = 'http://www.baidu.com'
# 模拟请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/60.0.3112.113 Safari/537.36'
}

# 设置一个请求体
req = urllib.request.Request(url, headers=headers)

# 发起请求
response = urllib.request.urlopen(req)
data = response.read().decode('utf-8')
print(data)
