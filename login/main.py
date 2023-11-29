# -*- coding: utf-8 -*-
"""
文件:main.py
创建者:QE
时间:2023/7/8 17:23
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
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from login import Ui_Form
class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    @pyqtSlot()
    def on_ok_clicked(self):
        user=self.user.text()
        password=self.password.text()
        if user=="admin":
            if password=="123456":
                QMessageBox.information(self,'消息','登录成功')
            else:
                QMessageBox.critical(self, '消息', '密码错误')
        else:
            QMessageBox.critical(self, '消息', '用户名错误')
    @pyqtSlot()
    def on_loser_clicked(self):
        self.close()
    def paintEvent(self, a0:QPaintEvent) -> None:
        p=QPainter(self)
        img=QPixmap('image/29.jpg')
        p.drawPixmap(self.rect(),img)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())