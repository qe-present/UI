# -*- coding: utf-8 -*-
"""
文件:gif.py
创建者:QE
时间:2023/7/10 13:15
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
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.__initui()
    def __initui(self):
        self.resize(450,450)
        gif=QMovie('image/moon.gif')
        l=QLabel(self)
        l.setMovie(gif)
        gif.start()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())
