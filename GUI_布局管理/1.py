#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1.py
# @Time      :2020/12/30 0:07
# @Author    :Jinzhiliang

import pandas as pd
import os
curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = curPath[:curPath.find("myProject\\")+len("myProject\\")]  # 获取myProject，也就是项目的根路径
print(rootPath)
dataPath = os.path.abspath(rootPath + 'data\\GUI_cal.py') # 获取tran.csv文件的路径
print(dataPath)
trainData = pd.read_csv(dataPath )
print(trainData)