# -*-coding:utf-8-*-
from urllib import request


url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b' \
      '9999_10000&sec=1548865095761&di=629c1fa056cd032b2320d6a3126' \
      'b378c&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fupl' \
      'oads%2Fitem%2F201505%2F30%2F20150530093303_atUNP.jpeg'
filepath = url.split('_')[-1]
request.urlretrieve(url, filepath)

