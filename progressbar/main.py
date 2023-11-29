# -*- coding: utf-8 -*-
"""
文件:main.py
创建者:QE
时间:2023/8/5 13:39
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

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

qss = """
QProgressBar{
    text-align:center;
    border:1px groove blue;
}
QProgressBar::chunk{
    background-color:blue;
}
"""


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.now_value = 0
        self.resize(640, 480)
        self.__initui()

    def __initui(self):
        btn = QPushButton('开始', self)
        btn.clicked.connect(self.start_bar)
        self.bar = QProgressBar(self)
        self.bar.setStyleSheet(qss)
        self.bar.setGeometry(100, 100, 400, 30)
        self.bar.setRange(0, 5)
        self.bar.setValue(self.now_value)
        self.bar.setFormat('下载音乐 %p%')
        self.timer = QTimer(self, timeout=self.ok)

    def start_bar(self):
        self.timer.start(1000)

    def ok(self):
        self.now_value += 1
        print(self.now_value)
        if self.now_value == self.bar.maximum():
            self.timer.stop()
        self.bar.setValue(self.now_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    h = Main()
    h.show()
    sys.exit(app.exec_())
