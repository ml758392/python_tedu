# -*-coding:utf-8-*-
import urllib.request

url = r'https://www.baidu.com/s?wd=%E9%99%88%E9%83%BD%E7%81%B5&rsv_spt=1&rsv_iqid=0x8216f60e0003f87f&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug2=0&inputT=11319&rsv_sug4=12056'

newurl = urllib.request.unquote(url)    # 解码
print(newurl)


oldurl = urllib.request.quote(newurl)   # 编码
print(oldurl)                           # 编码之后的url才能访问成功

