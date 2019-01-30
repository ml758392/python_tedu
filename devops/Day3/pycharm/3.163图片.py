# -*-coding:utf-8-*-
from urllib import request
import re
import os


def get_file(url, name):
    html = request.urlopen(url)
    with open(name, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)


def get_url(patt, fname, charset='utf8'):
    url_list = []   # 将匹配的网址放到列表中
    cpatt = re.compile(patt)
    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                url_list.append(m.group())
    return url_list


def main():
    url_163 = 'http://www.163.com'
    fname_163 = '/tmp/163.html'
    get_file(url_163, fname_163)
    img_patt = r'(http|https)://[\w./]+\.(jpg|png|gif|png)'
    pic_url = get_url(img_patt, fname_163, 'GBK')

    dst = '163pic'
    if not os.path.exists(dst):
        os.mkdir(dst)
    for url in pic_url:
        fname = url.split('/')[-1]
        fname = os.path.join(dst, fname)
        get_file(url, fname)


if __name__ == '__main__':
    main()
