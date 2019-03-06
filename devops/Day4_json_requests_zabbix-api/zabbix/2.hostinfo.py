# -*-coding:utf-8-*-
import json
import requests


url = 'http://127.0.0.1/api_jsonrpc.php'
header = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1,
    # "auth": null
}

r = requests.post(url=url, data=json.dumps(data), headers=header)
# print(r.json())
result = r.json()
auth = result["result"]

data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
    },
    "auth": auth,
    "id": 1
}
r = requests.post(url, data=json.dumps(data), headers=header)
print(r.text)
# print(r.json())
# python3 /root/桌面/5_张志刚/devops/Day4_json_requests_zabbix-api/zabbix/2.hostinfo.py  | python3 -m json.tool

#########################################################
# 将主机ID是10257和10258的主机从zabbix之中删除
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "hostid",
#         "hostid"
#     ],
#     "auth": auth
#     "id": 1
# }


#########################################################
# # 创建主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.create",
#     "params": {
#         "host": "web1_server1",
#         "interfaces": [
#             {
#                 "type": 1,
#                 "main": 1,
#                 "useip": 1,
#                 "ip": "192.168.4.1",
#                 "dns": "",
#                 "port": "10050"
#             }
#         ],
#         "groups": [
#             {
#              "groupid": "50"
#             }
#         ],
#         "templates": [
#             {
#                 "templateid": "20045"
#             }
#         ],
#         "inventory_mode": 0,
#         "inventory": {
#             "macaddress_a": "01234",
#             "macaddress_b": "56768"
#         }
#     },
#     "auth": auth
#     "id": 1
# }

#########################################################






