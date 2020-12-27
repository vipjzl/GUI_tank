#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :first_GUI.py
# @Time      :2020/12/26 20:09
# @Author    :Jinzhiliang

from tkinter import *
# 创建窗口对象
# from tkinter import messagebox
from tkinter import messagebox

root=Tk()


# 定义一个事件,按钮Button事件
btn01=Button(root)
btn01['text']='点我就送花'

btn01.pack()

def songhua(e):
    messagebox.showinfo('Message','送你玫瑰花')
    print('送你一朵花')

btn01.bind('<Button-1>',songhua)

root.title('第一个GUI窗口')
root.iconbitmap('/icon.ico')
root.geometry('300x300+200+300')  #'wxh+x+y'







# 运行组件,显示窗口.类似一个死循环
root.mainloop()



