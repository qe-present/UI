# -*- coding: utf-8 -*-
"""
文件:3.py
创建者:QE
时间:2023/8/10 22:23
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

import numpy as np
import pandas as pd
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from tables import Ui_Form

class TableWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableWindow()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_read_clicked(self):
        path, ok = QFileDialog.getOpenFileName(self, '读取csv文件', '', '(*.csv)')
        if path:
            data = pd.read_csv(path)
        self.title = list(data)
        self.content = np.array(data).tolist()
        self.__init_title()
    @pyqtSlot()
    def on_init_clicked(self):
        pass
    @pyqtSlot()
    def on_loser_clicked(self):
        self.close()


    def __init_title(self):
        column = self.ui.tableWidget.columnCount()
        for i, t in enumerate(self.title):
            self.ui.tableWidget.insertColumn(column)
            item = QTableWidgetItem(t)
            self.ui.tableWidget.setHorizontalHeaderItem(i, item)
            column += 1


if __name__ == '__main__':
    app = QApplication([])
    win = TableWindow()
    win.show()
    sys.exit(app.exec_())
