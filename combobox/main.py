# -*- coding: utf-8 -*-
"""
文件:main.py
创建者:QE
时间:2023/7/17 15:19
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
from com import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.sql='create table if not exists student(\n'
        self.q=QLineEdit()
        self.setupUi(self)
    def ok_clicked(self):
        word=self.word.text()
        word_type=self.word_type.currentText()
        identity=self.get_data(self.identity.ok)
        s=word+" "+word_type+" "+identity+',\n'
        self.sql+=s
        print(self.sql)

    def get_data(self,t):
        s=''
        for i in t:
            match i:
                case 'PK':
                    s += 'primary key'
                case 'NN':
                    s += 'not null'
                case 'UQ':
                    s += 'unique'
                case 'BIN':
                    s += 'binar'
                case 'UN':
                    s += 'unsigned'
                case 'ZF':
                    s += 'zero fill'
                case 'AL':
                    s += ' auto_increment'
                case 'G':
                    s += 'generated column'
        return s
    def type_change(self,index):
        if index==1:
            self.word_type.setLineEdit(self.q)
            self.q.setReadOnly(False)
        else:
            self.q.setReadOnly(True)
    def id_change(self,index):
        pass
    def closeEvent(self, a0):
        end='\n)engine=innoDB default charset=utf8;'
        self.sql=self.sql[:-2]+end
        print(self.sql)







if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())
