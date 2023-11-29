# -*- coding: utf-8 -*-
"""
文件:al.py
创建者:QE
时间:2023/7/15 14:20
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
from PyQt5.QtWidgets import QDialog,QLabel,QLineEdit,QVBoxLayout,QHBoxLayout,QApplication,QPushButton
import sys
class Alter(QDialog):
    def __init__(self,title,content):
        super().__init__()
        self.title=title
        self.content=content
        self.now_content=[]
        self.data=[]

        self.__initui()
    def __initui(self):
        self.resize(640,480)
        self.put_data()
    def put_data(self):

        v=QVBoxLayout(self)
        for i,j in zip(self.title,self.content):
            h=QHBoxLayout()
            q=QLabel(str(i),self)
            e=QLineEdit(str(j),self)
            self.data.append(e)
            h.addWidget(q)
            h.addWidget(e)
            v.addLayout(h)
        h = QHBoxLayout()
        ok=QPushButton('确定')
        ok.clicked.connect(self.on_clicked)
        loser=QPushButton('取消')
        loser.clicked.connect(self.loser_clicked)
        h.addWidget(ok)
        h.addWidget(loser)
        v.addLayout(h)
    def on_clicked(self):
        for i in self.data:
            i:QLineEdit
            self.now_content.append(i.text())
        self.accept()
    def loser_clicked(self):
        self.close()







if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Alter([1,2,3],['ssfs','asda','gyh'])
    h.show()
    sys.exit(app.exec_())