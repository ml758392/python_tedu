# -*-coding:utf-8-*-
import tkinter


# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title("YY")

# 设置大小和位置   长x宽  距离
win.geometry('400x400+200+200')


def showinfo():
    print(entry.get())


entry = tkinter.Entry(win)
entry.pack()

button =tkinter.Button(win, text='提交', command=showinfo)
button.pack()











# 进入消息循环
win.mainloop()

if __name__ == '__main__':
    pass
