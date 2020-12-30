#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Gui_to_object.py
# @Time      :2020/12/26 20:34
# @Author    :Jinzhiliang

"""
Entry单选文本,制作登录界面
"""
from tkinter import *
from tkinter import messagebox

global user_Name
global user_Pw


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)    # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createwidget()

    # 创建自己的组件
    def createwidget(self):
        # 创建登录的组件
        self.lb02 = Label(
            self,
            text='用户名',
            width=10,
            height=2,
            # bg='black',
            # fg='white',
            font=('宋体', 10))
        self.lb02.pack()

        user_Name = StringVar()
        # user_Name = IntVar()
        print(type(user_Name))
        print(user_Name)
        self.entry01 = Entry(
            self,
            textvariable=user_Name.get()
        )
        self.entry01.pack()  # pack就是将事件布局到主窗口中
        # user_Name.set('admin1')
        # print(user_Name.get())
        # print(self.entry01.get())

        self.lb02 = Label(
            self,
            text='密码',
        )
        self.lb02.pack()

        user_Pw = StringVar()
        # user_Pw = IntVar()
        print(type(user_Pw))    # <class 'tkinter.StringVar'>
        print(user_Pw)          # PY_VAR1
        self.entry02 = Entry(
            self,
            textvariable=user_Pw.get(),
            # show='*',
        )

        self.entry02.pack()  # pack就是将事件布局到主窗口中
        # user_Pw.set('admin1')
        # print('user_Pw\'get:',user_Pw.get())
        # print('entry02\'get:',self.entry02.get())

        self.btn01 = Button(self, text='登录', command=self.login)
        self.btn01.pack()

    def login(self):
        # self.btn01.config(
        #     state='enabled'
        # )
        if self.entry01.get() == 'cheny' and self.entry02.get() == '12345':
            messagebox.showinfo('逻辑教育课堂', '您好' + self.entry01.get() + ',你已成功进入逻辑教育课程,欢迎!')
        else:
            messagebox.showinfo('登录失败', '登录失败,用户名或密码错误,请重新登录')


def main():
    root = Tk()
    root.geometry('240x260+200+300')
    root.title('系统登录')

    app = Application(master=root)

    root.mainloop()


if __name__ == '__main__':
    main()
