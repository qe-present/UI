
# -*- coding: utf-8 -*-
"""
文件:UI/手写签名/main.py
创建者:QE
时间:2023/8/24 15:25
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
from hand import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from spiders import DownLoadSpider
class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.img=QPixmap()
        self.border_color_text = None
        self.font_color_text = None
        self.color_dialog=QColorDialog()
        self.setupUi(self)
        self.__initui()
    def __initui(self):
        self.web_font.get_url='http://www.jiqie.com/a/15.htm'
    def set_img(self):
        scene=QGraphicsScene()
        scene.addPixmap(self.img)
        self.graphicsView.setScene(scene)
    @pyqtSlot()
    def on_font_color_clicked(self):
        self.font_color_text=self.get_color()
        self.font_color.setStyleSheet(f'background-color:{self.font_color_text}')
    @pyqtSlot()
    def on_border_color_clicked(self):
        self.border_color_text=self.get_color()
        self.border_color.setStyleSheet(f'background-color:{self.border_color_text}')
    def get_color(self):
        accept=self.color_dialog.exec_()
        if accept:
            return self.color_dialog.currentColor().name()
    @pyqtSlot(name='on_sure_clicked')
    def a(self):
        text=self.input_text.text()
        if text:
            spider=DownLoadSpider(text,
                                  self.web_font.get_current_value(),
                                  self.font_color_text,
                                  self.border_color_text,
                                  )
            spider.start()
            spider.join()
            self.img.loadFromData(spider.content)
            self.set_img()
        else:
            print('请输入文字！！！')
    @pyqtSlot()
    def on_save_clicked(self):
        filename,_=QFileDialog.getSaveFileName(self,'保存文件','','*.jpg')
        if filename:
            self.img.save(filename)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.showMaximized()
    sys.exit(app.exec_())