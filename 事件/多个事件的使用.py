# -*- coding: utf-8 -*-
"""
文件:UI/事件/多个事件的使用.py
创建者:QE
时间:2023/8/19 14:00
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
"""
实现图片的放大,旋转、移动
"""
# -*- coding: utf-8 -*-
"""
文件:UI/事件/多个事件的使用.py
创建者:QE
时间:2023/8/19 14:00
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
"""
实现图片的放大,旋转、移动
"""
import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import Qt,QRect,QPoint,QSize
from PyQt5.QtGui import QWheelEvent,QPainter,QPixmap,QKeyEvent,QPaintEvent,QMouseEvent,QTransform
class Main(QWidget):

    start=QPoint()
    rect_xy=QPoint()
    rect_wh=QSize()
    transform=QTransform()
    scale=1
    now_btn=None
    now_x=0
    now_y=0
    dx=0
    dy=0
    right_rotate=False
    now_angle=0
    painter = QPainter()
    def __init__(self):
        super().__init__()
        self.pixmap = QPixmap('../login/image/29.jpg')
    def rect(self) -> QRect:
        return QRect(
            self.rect_xy,
            self.rect_wh
        )
    def wheelEvent(self, a0: QWheelEvent) -> None:
        angel=int(a0.angleDelta().y()/8)
        if angel>0:
            self.scale+=0.1
        else:
            self.scale-=0.1
        self.update()
    def mousePressEvent(self, a0: QMouseEvent) -> None:
        btn=a0.button()
        if btn==Qt.LeftButton:
            self.start=a0.pos()-self.rect_xy
            self.now_btn=btn
        elif btn==Qt.RightButton:
            self.now_btn=btn
    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        btn = a0.button()
        if btn == Qt.LeftButton:
            self.now_x=self.rect_xy.x()
            self.now_y=self.rect_xy.y()
        if btn==Qt.RightButton:
            self.now_btn='relese'
            self.painter.translate(0,0)
            self.rect_xy.setX(self.now_x)
            self.rect_xy.setY(self.now_y)
        else:
            pass
    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if self.now_btn==Qt.LeftButton:
            self.rect_xy=a0.pos()-self.start
            self.update()
        if self.now_btn==Qt.RightButton:
            b=a0.pos()-self.start
            self.dx = self.now_x+self.rect_wh.width() / 2
            self.dy = self.now_y+self.rect_wh.height() / 2
            self.now_angle=b.y()
            self.update()
    def paintEvent(self, a0: QPaintEvent) -> None:
        self.painter.begin(self)
        if self.scale>0:
            self.rect_wh.setWidth(int(self.pixmap.width()*self.scale))
            self.rect_wh.setHeight(int(self.pixmap.height()*self.scale))
        if self.now_btn==Qt.RightButton:
            self.painter.translate(self.dx,self.dy)
            self.rect_xy.setX(-int((self.now_x+self.rect_wh.width()) / 2))
            self.rect_xy.setY(-int((self.now_y+self.rect_wh.width())/ 2))
            self.painter.rotate(self.now_angle)
        self.painter.drawPixmap(self.rect(),self.pixmap)
        self.painter.end()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())


