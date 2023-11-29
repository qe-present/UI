# -*- coding: utf-8 -*-
"""
文件：UI/control/adjustcombobox.py
创建者：QE
诗：
    鲸鱼安慰了大海
            - 燕七
    不是所有的树
    都能在自己的家乡终老
    不是所有的轨道
    都通往春暖花开的方向
    不是所有的花都会盛开
    不是所有约定的人都会到来
    我知道，是流星赞美了黑夜
    鲸鱼安慰了大海
"""
from PyQt5.QtWidgets import QComboBox,QWidget,QApplication,QPushButton
import sys
class AdjustCombobox(QComboBox):
    def get_max_width(self):
        item_list=[]
        for i in range(self.count()):
            item_list.append(len(self.itemText(i)))
        return max(item_list)

    def adjustSize(self) -> None:
        item_length=self.get_max_width()
        add_length=item_length*11
        now_length=38+add_length
        self.resize(now_length,self.height())