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
from PyQt5.QtSql import QSqlDatabase, QSqlQuery,QSqlQueryModel
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSlot, QDate, QDateTime,Qt
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from tool.logger import logger
import sys


class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.now_databse = None
        self.model=QSqlQueryModel()
        self.tableView.setModel(self.model)
        self.__initui()

    def __initui(self):
        self.db = self.__open_mysql()
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
    @pyqtSlot(str)
    def on_db_com_currentTextChanged(self, text):
        self.now_databse = text
        self.__init_table()
        self.on_sure_clicked()
    def on_sure_clicked(self):
        self.model.clear()
        table=self.table_com.currentText()
        ok=self.query.exec_(f'select * from {table}')
        if ok:
            self.model.setQuery(self.query)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    h = Main()
    sys.exit(app.exec_())