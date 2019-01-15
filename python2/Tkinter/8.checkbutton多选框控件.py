# -*-coding:utf-8-*-
import tkinter


win = tkinter.Tk()
win.title("YY")
win.geometry('400x400+200+200')


def updata():
    message = ''
    if hobby1.get():
        message += 'money\n'
    if hobby2.get():
        message += 'power\n'
    if hobby3.get():
        message += 'person\n'

    # 清除text中的所有内容
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)


hobby1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win, text='money',
                             variable=hobby1, command=updata)
check1.pack()

hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text='power',
                             variable=hobby2, command=updata)
check2.pack()

hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text='person',
                             variable=hobby3, command=updata)
check3.pack()


text = tkinter.Text(win, width=50, height=5)
text.pack()

win.mainloop()

