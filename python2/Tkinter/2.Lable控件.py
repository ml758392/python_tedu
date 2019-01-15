# -*-coding:utf-8-*-
import tkinter

win = tkinter.Tk()
win.title("YY")
win.geometry('400x400+200+200')

'''
Lable:标签控件可以显示文本

'''
# win  master 父窗体
# bg    背景色
# fg    字体颜色
# wraplength 指定text文本中多宽进行换行
# justify   对齐方式
# anchor    位置 n北 e东 s南 w西

label = tkinter.Label(win, text='yy is a good man',
                      bg='green', fg='black',
                      font=('黑体', 20),
                      width=40, height=3, wraplength=190,
                      justify='left', anchor='n')

# 显示出来
label.pack()






win.mainloop()