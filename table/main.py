# -*- coding: utf-8 -*-
"""
文件:main.py
创建者:QE
时间:2023/7/28 16:46
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
from create_table import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
OK=True
class ComboBox(QComboBox):
    class Listview(QListView):
        def __init__(self,parent=None):
            super().__init__(parent)
        def mousePressEvent(self, e):
            global OK
            OK=False
            super().mousePressEvent(e)

    def __init__(self,parent=None,init:[str]=None):
        super().__init__(parent)
        self.get_item=[]
        self.get_texts=[]
        self.init=init
        if self.init:
            self.__init_item(self.init)

        self.setView(self.Listview(self))
        self.activated.connect(self.change_ok)
        self.view().pressed.connect(self.get_data)
    def __init_item(self,a:[str]):
        self.addItems(a)
    def change_ok(self):
        global OK
        OK=True
    def hidePopup(self):
        if OK:
            super().hidePopup()
    def showPopup(self) -> None:
        super().showPopup()
        model=self.model()
        count=self.count()
        for i in range(count):
            index=model.index(i,0)
            standard_item: QStandardItem = model.itemFromIndex(index)
            cheched_state = standard_item.checkState()
            if cheched_state==2:
                standard_item.setCheckState(0)
        self.get_item.clear()
    def get_data(self,index):
        standard_model=self.model()
        standard_item=standard_model.itemFromIndex(index)
        cheched_state=standard_item.checkState()
        if not cheched_state:
            a=int(not cheched_state)+1
            standard_item.setCheckState(a)
            self.get_item.append(index.row())
        else:
            standard_item.setCheckState(not cheched_state)
            self.get_item.remove(index.row())
    @property
    def ok(self):
        if self.get_item:
            self.get_item.sort()
            self.get_texts.clear()
            for i in self.get_item:
                self.get_texts.append(self.itemText(i))
            return self.get_texts
class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__initui()
    def __initui(self):
        self.title=['字段','类型','符号']
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.init_header()
        self.tableWidget.setContextMenuPolicy(3)
    @pyqtSlot(QPoint)
    def on_tableWidget_customContextMenuRequested(self,pos):
        add=QAction('添加')
        add.setObjectName('add')
        add.triggered.connect(self.add_triggered)
        menu=QMenu()
        menu.addAction(add)
        menu.exec_(self.tableWidget.mapToGlobal(pos))
    def add_triggered(self):
        row=self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        for i,t in enumerate(self.get_content()):
            self.tableWidget.setCellWidget(row,i,t)


    def init_header(self):
        column=self.tableWidget.columnCount()
        for i,t in enumerate(self.title):
            self.tableWidget.insertColumn(column)
            item=QTableWidgetItem(str(t))
            self.tableWidget.setHorizontalHeaderItem(i,item)
            column+=1
    def get_content(self):
        return [QLineEdit(),QComboBox(self),ComboBox(self,init=self.init_content()),]
    def init_content(self):
        return ['PK','UN','NN','AL']


if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())