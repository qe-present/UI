# -*- coding: utf-8 -*-
"""
文件:UI/fontdialog/main.py
创建者:QE
时间:2023/8/19 13:26
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
from fontdialog import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__initui()
    def __initui(self):
        self.color_dialog=QColorDialog()
        p=self.label.palette()
        label_color=p.color(QPalette.ColorRole.WindowText)
        self.color_dialog.setCurrentColor(label_color)

        self.font_dialog=QFontDialog()
        self.label_font=self.label.font()
        self.font_dialog.setCurrentFont(self.label_font)
        self.font_com.setCurrentFont(self.label_font)

    @pyqtSlot()
    def on_color_clicked(self):
        accept=self.color_dialog.exec_()
        if accept:
            color=self.color_dialog.currentColor()
            palette=QPalette()
            palette.setColor(QPalette.WindowText,color)
            self.set_label(palette=palette)
    @pyqtSlot()
    def on_set_font_clicked(self):
        self.font_dialog.setCurrentFont(self.label_font)
        accept=self.font_dialog.exec_()
        if accept:
            font=self.font_dialog.currentFont()
            self.set_label(font=font)
    @pyqtSlot(QFont)
    def on_font_com_currentFontChanged(self,font:QFont):
        self.set_label(font=font)

    def set_label(self,palette:QPalette=None,font:QFont=None):
        if palette:
            self.label.setPalette(palette)
        if font:
            self.label.setFont(font)
            self.label_font = self.label.font()
    @staticmethod
    def main():
        app=QApplication(sys.argv)
        h = Main()
        h.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    Main.main()

