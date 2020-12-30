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

        self.btn01 = Button(self,
                            text='登录系统',
                            command=self.login)
        self.btn01.pack()  # pack就是将事件布局到主窗口中

        self.btn02=Button(self,text='退出',command=root.destroy)
        self.btn02.pack()

        global im
        im=PhotoImage(file='image/player1.gif')
        self.btn02=Button(self,image=im,command=self.login)
        self.btn02.pack()

        # # 设置禁用状态
        # self.btn02.config(
        #     state='disabled'
        # )

    def login(self):
        # self.btn02.config(
        #     state='disabled'
        # )
        messagebox.showinfo('Message', '登录成功,欢迎!')


root=Tk()
root.geometry('300x300+400+300')
root.title('GUI的Button')

app=Application(master=root)

root.mainloop()

