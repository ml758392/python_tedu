# -*-coding:utf-8-*-
import requests

header = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
r = requests.get('http://127.0.0.1/ban', headers=header)

# tail -f /var/log/httpd/access_log
print(r.status_code)