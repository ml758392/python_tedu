# -*-coding:utf-8-*
from email.mime.text import MIMEText
from email.header import Header
import smtplib


# 邮件正文，纯文本，字符编码
message = MIMEText('Python邮件发送测试\n', 'plain', 'utf8')
message['From'] = Header('zzg@tedu.cn', 'utf8')   # 收件人
message['To'] = Header('2431617074@qq.com' 'utf8')  # 发件人
smtp = smtplib.SMTP('localhost')    # 本机作为邮件服务器发送邮件
sender = 'zzg@tedu.cn'
receivers = ['2431617074@qq.com', 'root@lenovo']
smtp.sendmail(sender, receivers, message.as_string())
