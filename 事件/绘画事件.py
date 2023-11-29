# -*- coding: utf-8 -*-
"""
文件:绘画事件.py
创建者:QE
时间:2023/8/14 13:51
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
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.__initui()
    def __initui(self):
        pass
    def paintEvent(self, a0:QPaintEvent):
        p=QPainter(self)
        pen=QPen(Qt.blue,30)
        p.setPen(pen)
        p.drawLine(10,10,10,300)
        p.setFont(QFont('simsun',50))
        p.drawText(40,40,100,100,Qt.AlignLeft,'asdsdf')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())
