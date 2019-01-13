# -*-coding:utf-8-*-
import urllib.request


def imagecrawler(url, topath):
    headers ={
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb\
            Kit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    Htmlstr = response.read().decode('utf-8')

    pat = r''