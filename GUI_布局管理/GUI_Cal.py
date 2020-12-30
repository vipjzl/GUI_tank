#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :GUI_Cal.py
# @Time      :2020/12/29 22:01
# @Author    :Jinzhiliang

"""计算器软件界面的设计"""

from tkinter import *
from tkinter import messagebox
import random


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """通过 grid 布局实现计算器的界面"""
        btnText = (
            ("MC", "M+", "M-", "MR"),
            ("C", "±", "/", "✖ "),
            (7, 8, 9, "-"),
            (4, 5, 6, "+"),
            (1, 2, 3, "="),
            (0, ".")
        )
        """
         enumerate:对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），
         enumerate将其组成一个索引序列，利用它可以同时获得索引和值
         (0, seq[0]), (1, seq[1]), (2, seq[2])
        """
        Entry(self).grid(row=0, column=0, columnspan=4, pady=10)
        for rindex, r in enumerate(btnText):  #两层循环分别取出行列的值
            for cindex, c in enumerate(r):

                if c == "=":
                    Button(self, text=c, width=4).grid(row=rindex + 1, column=cindex, rowspan=2, sticky=NSEW)
                elif c == 0:
                    Button(self, text=c, width=4).grid(row=rindex + 1, column=cindex, columnspan=2, sticky=NSEW)
                elif c == ".":
                    Button(self, text=c, width=4).grid(row=rindex + 1, column=cindex + 1, sticky=NSEW)
                else:
                    Button(self, text=c, width=4).grid(row=rindex + 1, column=cindex, sticky=NSEW)


if __name__ == '__main__':
    root = Tk()
    root.geometry("180x230+200+300")
    app = Application(master=root)
    root.mainloop()
