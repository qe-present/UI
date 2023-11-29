import sys

import numpy as np

from tables import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
from al import Alter

class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.data = None
        self.path = None
        self.content = None
        self.title = None
        self.setupUi(self)
        self.__initui()
    def __initui(self):
        self.query.setVisible(False)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
    @pyqtSlot(QPoint)
    def on_tableWidget_customContextMenuRequested(self,pos):
        if self.path:
            menu=QMenu()
            insert=menu.addAction('插入')
            add=menu.addAction('增加')
            a=menu.exec_(self.tableWidget.mapToGlobal(pos))
            if a==insert:
                rows = self.tableWidget.selectionModel().selectedRows()
                if len(rows)<1:
                    return
                for i in rows:
                    self.tableWidget.insertRow(i.row()+len(rows))
            if a==add:
                self.on_add_clicked()
    @pyqtSlot()
    def on_query_clicked(self):
        # 查询有问题
        word=self.word.currentText()
        symbol=self.symbol.currentText()
        word_content=self.word_content.text()
        sql=''
        if symbol=='=':
            symbol='=='
        if symbol=='like':
            self.data[f'{word}']=self.data[f'{word}'].astype(str)
            sql="""self.data.query(f'{word}.str.contains("{word_content}")')"""
        else:
            sql=f'self.data.loc[(self.data["{word}"]{symbol}{word_content})]'
        result_set=eval(sql)
        print(result_set)
        if result_set:
            result_list=result_set.values.tolist()
            self.tableWidget.setRowCount(0)
            row = self.tableWidget.rowCount()
            for i in result_list:
                self.tableWidget.insertRow(row)
                for column, s in enumerate(i):
                    item = QTableWidgetItem(str(s))
                    self.tableWidget.setItem(row, column, item)
                row += 1
        else:
            pass

    @pyqtSlot()
    def on_read_clicked(self):
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.path,ok=QFileDialog.getOpenFileName(self,'读取csv文件','','(*.csv)')
        if self.path:
            self.query.setVisible(True)
            self.data=pd.read_csv(self.path)
            self.title=list(self.data)
            self.__init_title()
            self.init_clicked()
            self.init_word()
    def init_word(self):
        self.word.addItems(self.title)
        self.word.adjustSize()

    def init_clicked(self):
        self.data: pd.DataFrame
        for row in range(self.data.shape[0]):
            self.tableWidget.insertRow(row)
            for col in range(self.data.shape[1]):
                item=QTableWidgetItem(str(self.data.iat[row,col]))
                self.tableWidget.setItem(row,col,item)



    @pyqtSlot()
    def on_loser_clicked(self):
        self.close()
    def __init_title(self):
        column=self.tableWidget.columnCount()
        for i,t in enumerate(self.title):
            self.tableWidget.insertColumn(column)
            item=QTableWidgetItem(str(t))
            self.tableWidget.setHorizontalHeaderItem(i,item)
            column+=1
    @pyqtSlot()
    def on_add_clicked(self):
        if self.path:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
    @pyqtSlot()
    def on_delete_btn_clicked(self):
        rows=self.tableWidget.selectionModel().selectedRows()
        rows.reverse()
        for i in rows:
            self.tableWidget.removeRow(i.row())
    @pyqtSlot()
    def on_save_clicked(self):
        self.get_all_data()
        df=pd.DataFrame(self.content)
        df.to_csv(self.path,header=self.title,index=False)
    @pyqtSlot()
    def on_alter_clicked(self):
        rows = self.tableWidget.selectionModel().selectedRows()
        if rows:
            for i in rows:
                alter=Alter(self.title,self.get_one_content(i.row()))
                end=alter.exec_()
                if end==QDialog.Accepted:
                    now_content=alter.now_content
                    if now_content:
                        for j,text in enumerate(now_content):
                            item=self.tableWidget.item(i.row(),j)
                            if item:
                                item.setText(text)

    def get_one_content(self,row):
        content=[]
        for i in range(len(self.title)):
            item=self.tableWidget.item(row, i)
            if item:
                content.append(item.text())
        return content

    def get_all_data(self):
        self.content:list
        if self.content:
            self.content.clear()
            for i in range(self.tableWidget.rowCount()):
                column_data=[]
                for j in range(self.tableWidget.columnCount()):
                    item=self.tableWidget.item(i,j)
                    if item:
                        column_data.append(item.text())
                self.content.append(column_data)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())