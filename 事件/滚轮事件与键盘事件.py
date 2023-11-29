# -*- coding: utf-8 -*-
"""
文件:UI/事件/滚轮事件与键盘事件.py
创建者:QE
时间:2023/8/18 12:59
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
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent,QWheelEvent,QKeyEvent,QKeySequence
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.btn_x=100
        self.btn_y=100
        self.btn_w=70
        self.btn_h=30
        self.__initui()
    def __initui(self):
        self.btn=QPushButton('确定',self)
        self.set_btn_position()
    def set_btn_position(self):
        self.btn.setGeometry(self.btn_x,self.btn_y,self.btn_w,self.btn_h)
    def wheelEvent(self, a0: QWheelEvent) -> None:
        angle=int(a0.angleDelta().y()/40)
        if self.btn_w>0 and self.btn_h>0:
            self.btn_h+=angle
            self.btn_w+=angle
        self.set_btn_position()
    def keyPressEvent(self, a0: QKeyEvent) -> None:
        key=a0.key()
        match key:
            case Qt.Key_W:
                self.btn_y-=10
            case Qt.Key_S:
                self.btn_y+=10
            case Qt.Key_A:
                self.btn_x-=10
            case Qt.Key_D:
                self.btn_x+=10
        self.set_btn_position()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())
