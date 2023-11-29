# -*- coding: utf-8 -*-
"""
文件：UI/tableview/main.py
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
"""
表 
"""
from view import Ui_Form
from PyQt5.QtSql import QSqlDatabase, QSqlQuery,QSqlQueryModel,QSqlTableModel
from PyQt5.QtWidgets import QWidget, QApplication,QHeaderView,QFileDialog
from PyQt5.QtCore import pyqtSlot, QDate, QDateTime,Qt,QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from tool.logger import logger
import sys


class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.now_databse = None
        self.now_table=None
        self.now_use_table=None
        self.now_table_all_count=0
        self.start_count=0
        self.all_page=0
        self.page_count=11
        self.__initui()

    def __initui(self):
        self.db = self.__open_mysql()
        self.model=QSqlTableModel(self,self.db)
        self.model.setObjectName('qsqltablemodel')
        self.tableView.setModel(self.model)
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.now_page.setMinimum(1)
        self.query = QSqlQuery(self.db)
        self.__init_db()
        self.__init_table()

    def __init_db(self):
        ok = self.query.exec_('show databases')
        db_list = []
        while self.query.next():
            db_list.append(self.query.value(0))
        self.db_com.addItems(db_list)
        self.db_com.adjustSize()
        logger.info('初始化数据库成功')

    def __init_table(self):
        self.table_com.clear()
        ok=self.query.exec_(f'use {self.now_databse}')
        if ok:
            self.query.exec_('show tables')
            table_list = []
            while self.query.next():
                table_list.append(self.query.value(0))
            self.table_com.addItems(table_list)
            self.table_com.adjustSize()

    def __open_mysql(self):
        db = QSqlDatabase('QMYSQL')
        db.setHostName('127.0.0.1')
        db.setPort(3306)
        db.setUserName('root')
        db.setPassword('123456')
        if db.open():
            logger.info('mysql打开成功')
            self.show()
            return db
        else:
            logger.info('打开失败')
    @pyqtSlot()
    def on_to_csv_clicked(self):
        now_table=self.now_table
        csv_path=self.get_csv_path()
        csv_format="""fields terminated by ","  escaped by '' optionally enclosed  by ''   lines terminated by '\n'"""
        csv_sql=f"""select * from {now_table} into outfile '{csv_path}' {csv_format}"""
        ok=self.query.exec_(csv_sql)
        print(ok)
    @pyqtSlot(str)
    def on_db_com_currentTextChanged(self, text):
        self.now_databse = text
        self.__init_table()
        self.on_sure_clicked()
    @pyqtSlot(str)
    def on_table_com_currentTextChanged(self, text):
        self.now_table=text
        self.on_sure_clicked()
    def on_sure_clicked(self):
        self.model.clear()
        self.now_use_table=self.table_com.currentText()
        self.model.setTable(self.now_use_table)
        self.model.select()
        self.now_table_all_count=self.model.rowCount()
        if self.now_table_all_count>0:
            self.get_page()
            self.model.setFilter(f'1=1 limit {self.page_count}')
    @pyqtSlot()
    def on_add_btn_clicked(self):
        a=self.model.rowCount()
        self.model.insertRow(a)
    @pyqtSlot()
    def on_del_btn_clicked(self):
        rows=self.tableView.selectionModel().selectedRows()
        rows.reverse()
        for i in rows:
            self.model.removeRow(i.row())
    @pyqtSlot(int)
    def on_now_page_valueChanged(self,index):
        self.model.setFilter(f'1=1 limit {(index-1)*self.page_count},{self.page_count}')
    def get_page(self):
        self.all_page, leftover = divmod(self.now_table_all_count, self.page_count)
        if leftover> 0:
            self.all_page += 1
        self.all_page_label.setText(f'共{self.all_page}页')
        self.now_page.setMaximum(self.all_page)
        self.now_page.setValue(1)
    def get_csv_path(self):
        path,_=QFileDialog.getSaveFileName(self,'csv文件','','*.csv')
        return path

if __name__ == '__main__':
    app = QApplication(sys.argv)
    h = Main()
    sys.exit(app.exec_())