# -*- coding: utf-8 -*-
"""
文件:event.py
创建者:QE
时间:2023/8/8 14:21
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
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPaintEvent
class Main(QWidget):
    def event(self,a0: QEvent) -> bool:
        print(a0)
        print(type(a0))
        return True
    def paintEvent(self, a0:QPaintEvent) -> None:
        pass
if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())
