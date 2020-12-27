#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Gui_to_object.py
# @Time      :2020/12/26 20:34
# @Author    :Jinzhiliang

from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    # 创建自己的组件
    def createWidget(self):
        # self.btn01=Button(self)
        # self.btn01['text'] = '点击送花'   #按钮的文本显示
        # self.btn01['command']=self.songhua  #声明调用什么方法
        self.btn01 = Button(self, text='点击送花', command=self.songhua)
        self.btn01.pack()  # pack就是将事件布局到主窗口中


        self.btn02=Button(self,text='退出',command=root.destroy)
        self.btn02.pack()

    def songhua(self):
        messagebox.showinfo('Message', '玫瑰花送你最帅的你')
        print('玫瑰花送你最帅的你')

root=Tk()
root.geometry('300x300+400+300')
root.title('GUI的经典类的写法')

app=Application(master=root)

root.mainloop()

