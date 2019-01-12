# -*-coding:utf-8-*-
import urllib.request
import ssl
import json


def ajaxcrawler(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb\
    Kit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }

    req = urllib.request.Request(url, headers=headers)

    # 不验证ssl
    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req, context=context)
    jsonStr = response.read().decode('utf-8')
    jsonData = json.loads(jsonStr)
    return jsonData


if __name__ == '__main__':
    # url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=80'
    # info = ajaxcrawler(url)
    # print(info)
    for i in (1,11):
        url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=80'
        info = ajaxcrawler(url)
        print(info)