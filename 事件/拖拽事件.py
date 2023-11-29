# -*- coding: utf-8 -*-
"""
文件:拖拽事件.py
创建者:QE
时间:2023/8/15 16:26
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

class Combobox(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
    def dragEnterEvent(self, e:QDragEnterEvent):
        data:QMimeData=e.mimeData()
        self.data=data
        if self.data.hasText():
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.addItem(self.data.text())
class Accept(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.com=Combobox(self)
        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)

class Send(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)
        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 450, 300, 150)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    s= Send()
    a=Accept()
    a.show()
    s.show()
    app.exec_()