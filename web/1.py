# -*- coding: utf-8 -*-
"""
文件：UI/web/1.py
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
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtWidgets import QWidget,QApplication
import sys
class A(QWidget):
    def __init__(self):
        super().__init__()
        self.connect_mysql()
    def connect_mysql(self):
        db = QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName('127.0.0.1')
        db.setPort(3306)
        db.setDatabaseName('worker')
        db.setUserName('root')
        db.setPassword('123456')
        if db.open():
            print(1)
            self.show()
        else:
            print(2)
            self.close()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=A()
    sys.exit(app.exec_())