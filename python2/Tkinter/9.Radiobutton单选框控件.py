# -*-coding:utf-8-*-
import tkinter


win = tkinter.Tk()
win.title('YY')
win.geometry('400x400+200+200')


def updata():
    print(r.get())


# 一组单选框要绑定同一个变量
r = tkinter.IntVar()
radiol1 = tkinter.Radiobutton(win, text='one', value=1,
                              variable=r, command=updata)
radiol1.pack()

radiol2 = tkinter.Radiobutton(win, text='two', value=2,
                              variable=r, command=updata)
radiol2.pack()


win.mainloop()