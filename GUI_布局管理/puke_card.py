#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :puke_card.py
# @Time      :2020/12/29 22:20
# @Author    :Jinzhiliang


"""扑克牌游戏的界面设计"""

from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """通过 place 布局管理器实现扑克牌位置控制"""
        # self.photo =
        PhotoImage(file=r"..\.\images\puke\puke1.gif")
        # self.puke1 = Label(self.master,image=self.photo)
        # self.puke1.place(x=10,y=50)
        self.photos = [PhotoImage(file=r"..\.\images\puke\puke" + str(i + 1) + ".gif") for i in range(10)]
        self.pukes = [Label(self.master, image=self.photos[i]) for i in range(10)]
        for i in range(10):
            self.pukes[i].place(x=10 + i * 40, y=50)
            # 为所有的 Label 增加事件处理
        self.pukes[0].bind_class("Label", "<Button-1>", self.chupai)  #将与puckes[0]相同的所有Lable的组件全部bind "<Button-1>"事件,响应chupai


    def chupai(self, event):
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_y())
        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x270+200+300")
    app = Application(master=root)
    root.mainloop()