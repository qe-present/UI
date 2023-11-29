# -*- coding: utf-8 -*-
"""
文件:UI/control/fontcombobox.py
创建者:QE
时间:2023/8/24 16:14
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
from PyQt5.QtWidgets import QWidget,QApplication,QComboBox,QPushButton
from .spider import Spider
class FontComboBox(QComboBox):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.__url=None
        self.font_lists=None
        self.font_list=[]
        self.font_value=[]
    @property
    def get_url(self):
        self.start_spider()
        return self.__url
    @get_url.setter
    def get_url(self,url):
        self.__url=url
        self.get_url


    def start_spider(self):
        spider = Spider(self.__url)
        spider.start()
        spider.join()
        self.font_lists=spider.font_list
        self.get_font()
        return None
    def get_font(self):
        for i in self.font_lists:
            i:dict
            self.font_list.append(*i.keys())
            self.font_value.append(*i.values())
        self.addItems(self.font_list)
    def get_current_value(self):
        return self.font_value[self.currentIndex()]
# class Main(QWidget):
#     def __init__(self):
#         super().__init__()
#         f=FontComboBox(self)
#         f.get_url='http://www.jiqie.com/a/15.htm'
#         print(f.get_url)
#
# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     h=Main()
#     h.show()
#     sys.exit(app.exec_())