# -*- coding: utf-8 -*-
"""
文件:main.py
创建者:QE
时间:2023/8/5 14:54
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
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
qss = """
QProgressBar::chunk{
    background-color:blue;
}
"""
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
    def initui(self):
        self.resize(640,480)
        btn=QPushButton('开始',self,clicked=self.ok)
        self.bar=QProgressDialog('下载音乐','取消',0,200000)
        a=self.bar.findChild(QProgressBar)
        a.setStyleSheet(qss)
        self.bar.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
    def ok(self):
        maxnum=self.bar.maximum()
        self.bar.show()
        for i in range(maxnum):
            self.bar.setValue(i)
            QApplication.processEvents()
            if self.bar.wasCanceled():
                return




if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())
