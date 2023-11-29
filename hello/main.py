# -*- coding: utf-8 -*-
"""
文件:main.py
创建者:QE
时间:2023/7/7 15:23
诗: 鲸鱼安慰了大海
            -燕七
    不是所有的树
    都能在自己的家乡终老
    不是所有的轨道
    都通往春暖花开的方向
    不是所有约定的人
    都会到来
    我知道，是流星赞美了黑夜
    鲸鱼安慰了大海
"""
import sys
from helloi import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())