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

        self.lb01 = Label(self, text='逻辑教育',width=10,height=2,bg='black',fg='white')
        self.lb01['text']='logic'
        self.lb01.config(bg='red',fg='white')
        self.lb01.pack()  # pack就是将事件布局到主窗口中

        self.lb02=Label(self,text='cheny',width=10,height=2,bg='black',fg='white',font=('宋体',30))
        self.lb02.pack()

        global image
        image=PhotoImage(file=r'image/player1.gif')
        self.lb03=Label(self,image=image)
        self.lb03.pack()

        self.lb04 = Label(self,
                          text='cheny',
                          width=10,
                          height=2,
                          bg='black',
                          fg='white',
                          font=('宋体', 30),
                          board=1,
                          # relief=
                          )
        self.lb04.pack()

    def songhua(self):
        messagebox.showinfo('Message', '玫瑰花送你最帅的你')
        print('玫瑰花送你最帅的你')
if __name__ == '__main__':

    root=Tk()
    root.geometry('300x300+400+300')
    root.title('GUI的label标签的使用')

    app=Application(master=root)

    root.mainloop()

