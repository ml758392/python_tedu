# -*-coding:utf-8-*-
import tkinter


# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title("YY")

# 设置大小和位置   长x宽  距离
# win.geometry('400x400+200+200')

'''
文本控件，用于显示多行文本

'''

# 创建滚动条
scroll = tkinter.Scrollbar()


text = tkinter.Text(win, width=30, height=4)


# side放到窗体的那一侧,把Y轴填充满
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

text.pack(side=tkinter.LEFT, fill=tkinter.Y)

# 关联Text 和 scroll
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set )


str = '''你好，我是yy.
现在在测试Text控件功能
111
233
77
00000000
'''
text.insert(tkinter.INSERT, str)




# 进入消息循环
win.mainloop()

if __name__ == '__main__':
    pass
