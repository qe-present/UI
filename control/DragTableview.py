# -*- coding: utf-8 -*-
"""
文件:DragTableview.py
创建者:QE
时间:2023/8/16 15:57
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
from PyQt5.QtWidgets import QTableView
from PyQt5.QtGui import QDrag
from PyQt5.QtCore import QMimeData
class tableview(QTableView):
    DATA=None
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
    def startDrag(self, supportedActions) -> None:
        if self.DATA:
            index=self.currentIndex().row()
            index=19-index
            drag=QDrag(self)
            mimedata=QMimeData()
            mimedata.setText(str(index))
            drag.setMimeData(mimedata)
            drag.exec_()
        else:
            pass