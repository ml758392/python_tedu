# -*-coding:utf-8-*-
with open("/bin/ls", "rb") as a:
    while True:
        content = a.read(4096)      # 一次只缓存4096个字节
        if not content:             # 当content读取完毕，为False
            break
with open("/root/ls", "wb") as b:
    b.write(content)

