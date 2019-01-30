# -*-coding:utf-8-*-
from urllib import request


def get_data(url, name):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)


if __name__ == '__main__':
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548842575171&di=1880f7f17c854d6db4afb6cba7b9517e&imgtype=0&src=http%3A%2F%2Fp10.yokacdn.com%2Fpic%2FYOKA%2F2017-05-03%2FU445P1TS1493801093_97298.jpg'
    fname = '陈都灵小姐姐.jpg'
    get_data(url, fname)


#[root@lenovo ]# eog 陈都灵小姐姐.jpg
