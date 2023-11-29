# -*- coding: utf-8 -*-
"""
文件:main.py
创建者:QE
时间:2023/7/8 15:53
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
from button import Ui_Form
class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    @pyqtSlot()
    def on_ok_clicked(self):
        QMessageBox.information(self,'消息',self.sender().text())
    @pyqtSlot()
    def on_loser_clicked(self):
        self.close()
    @pyqtSlot(bool)
    def on_bold_clicked(self,checked):
        f=self.label.font()
        f.setBold(checked)
        self.label.setFont(f)
    def on_italic_toggled(self,checked):
        f=self.label.font()
        f.setItalic(checked)
        self.label.setFont(f)
    @pyqtSlot(bool)
    def on_underline_clicked(self,checked):
        f=self.label.font()
        f.setUnderline(checked)
        self.label.setFont(f)
    def on_red_toggled(self):
        p=self.label.palette()
        p.setColor(QPalette.WindowText,Qt.red)
        self.label.setPalette(p)
    def on_blue_toeeled(self):
        p=self.label.palette()
        p.setColor(QPalette.WindowText,Qt.blue)
        self.label.setPalette(p)
    def on_yellow_toggled(self):
        p=self.label.palette()
        p.setColor(QPalette.WindowText,Qt.yellow)
        self.label.setPalette(p)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())
