# -*- coding: utf-8 -*-
"""
文件:spin_main.py
创建者:QE
时间:2023/7/10 15:16
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
from spin import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__initui()
    def __initui(self):
        a=self.test_btn.geometry()
        self.x=a.x()
        self.y=a.y()
        self.w=a.width()
        self.h=a.height()
        self.now_w=self.w
        self.now_h = self.h
        self.r=0
        self.b=2
        self.width_spin.setValue(self.w)
        self.height_spin.setValue(self.h)
        self.r_spin.valueChanged.connect(self.change)
        self.b_spin.valueChanged.connect(self.change)
    def change(self,index):
        if self.sender().objectName()=='r_spin':
            self.r=index
        else:
            self.b=index
        css=f'border-radius:{self.r}px;border:{self.b}px groove blue'
        self.test_btn.setStyleSheet()

    @pyqtSlot(int)
    def on_width_spin_valueChanged(self,index):
        self.now_w=index
        self.test_btn.setGeometry(self.x,self.y,index,self.now_h)
    @pyqtSlot(int)
    def on_height_spin_valueChanged(self,index):
        self.now_h=index
        self.test_btn.setGeometry(self.x, self.y, self.now_w, index)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())