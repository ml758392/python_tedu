# -*-coding:utf-8-*-
import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title("YY")

# 设置大小和位置   长x宽  距离
win.geometry('400x400+200+200')


def func():
    print('yy')


# 创建按钮执行command命令
button1 = tkinter.Button(win, text='按纽1', command=func,
                        width=2, height=1)
button1.pack()


button2 = tkinter.Button(win, text='按纽2', command=lambda: print('lambda'),
                        width=2, height=1)
button2.pack()


# 退出按钮
Exit = tkinter.Button(win, text='exit', command=win.quit,
                      width=3, height=2)
Exit.pack()



# 进入消息循环
win.mainloop()

if __name__ == '__main__':
    pass
