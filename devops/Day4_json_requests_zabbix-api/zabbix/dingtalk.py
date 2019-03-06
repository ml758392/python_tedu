# -*-coding:utf-8-*-
import json
import requests
import sys


def send_msg(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,   # 不@所有人
        },
        "text": {
            "content": msg,     # 消息正文
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text


if __name__ == '__main__':
    msg = sys.argv[1]
    reminders = ['15937762237']  # 特别提醒要查看的人，就是@某人一下
    url = 'https://oapi.dingtalk.com/robot/send?access_token=f62936c2eb31a053f422b5fdea9ea4748ce873a399ab521ccbf3ec\
    29fefce9d1'
    print(send_msg(url, reminders, msg))

