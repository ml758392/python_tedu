# -*-coding:utf-8-*-
import urllib.request
import ssl

def qiudale(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb\
    Kit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url,header=header)
    response = urllib.request.urlopen(req, context=context)
    data = response.read().decode('utf-8')


# 未完待续


url = 'https://www.qiushibaike.com/text/page/2/'
info = qiudale(url)