# -*-coding:utf-8-*-
import json
import requests


url = 'http://127.0.0.1/api_jsonrpc.php'
header = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",  # 固定的 jsonrpc协议的版本
    "method": "apiinfo.version",  # 方法，在官方文档上查询
    "params": [],   # 参数
    "id": 1         # 随便给一个数字即可，表示任务的ID号
}
r = requests.post(url, data=json.dumps(data), headers=header)
print(r.json())
