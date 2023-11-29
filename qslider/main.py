# -*- coding: utf-8 -*-
"""
文件:main.py
创建者:QE
时间:2023/8/6 13:04
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
from slider import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__initui()

    def __initui(self):
        self.now_r = 0
        self.now_g = 0
        self.now_b = 0
        self.r.setRange(0, 255)
        self.g.setRange(0, 255)
        self.b.setRange(0, 255)
        self.font_size.setRange(0, 30)
        self.r.valueChanged.connect(self.change)
        self.g.valueChanged.connect(self.change)
        self.b.valueChanged.connect(self.change)
        self.font_size.sliderReleased.connect(self.font_change)
    def change(self, tick):
        p = self.label_5.palette()
        obj = self.sender()
        name = obj.objectName()
        match name:
            case 'r':
                self.now_r = tick
            case 'g':
                self.now_g = tick
            case 'b':
                self.now_b = tick
        p.setColor(QPalette.WindowText, QColor(self.now_r, self.now_g, self.now_b))
        self.label_5.setPalette(p)
    def font_change(self):
        size = self.font_size.value()
        font = self.label_5.font()
        font.setPointSize(size)
        self.label_5.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    h = Main()
    h.show()
    sys.exit(app.exec_())
