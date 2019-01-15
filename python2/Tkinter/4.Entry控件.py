# -*-coding:utf-8-*-
import tkinter


# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title("YY")

# 设置大小和位置   长x宽  距离
win.geometry('400x400+200+200')

'''
输入控件
用于显示简单的文本内容
'''
# 绑定变量
e = tkinter.Variable()

# show 密文显示
# show='*'
entry = tkinter.Entry(win, show='*', textvariable=e)
entry.pack()

# e 就代表输入框这个对象
# 设置值
e.set('sunck is a good man')
# 取值
print(e.get())
print(entry.get())




# 进入消息循环
win.mainloop()

if __name__ == '__main__':
    pass
