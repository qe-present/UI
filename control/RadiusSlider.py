# -*- coding: utf-8 -*-
"""
文件:RadiusSlider.py
创建者:QE
时间:2023/8/14 15:01
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
from PyQt5.QtWidgets import QSlider
from PyQt5.QtGui import QMouseEvent,QColor
from PyQt5.QtCore import pyqtSignal,Qt
from tool.qss_template import QssTemplate
class Slider(QSlider):
    choice={
        0:'sub_color',
        1:'handle_color',
        2:'add_color',
    }
    class ChoiceColor(int):
        SubcColor=0
        HandleColor=1
        AddColor=2
    valueChanged = pyqtSignal(int,int)
    def __init__(self, *__args):
        super().__init__(*__args)
        self.model = None
        self.slider_type=None
        self.__margin =4
        self.__finish=False
    def setOrientation(self,a0:Qt.Orientation):
        if a0==Qt.Horizontal:
            self.slider_type='horizontal'
            self.model=QssTemplate('hslider.qss')
        else:
            self.slider_type = 'vertical'
            self.model=QssTemplate('vslider.qss')
        super().setOrientation(a0)
    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        super().mouseReleaseEvent(ev)
        self.valueChanged.emit(self.value(),0)
    def setGeometry(self,*__args):
        super().setGeometry(*__args)
    def mousePressEvent(self, ev:QMouseEvent) -> None:
        super().mousePressEvent(ev)
        value_range=self.maximum() - self.minimum()
        pos =self.minimum() + value_range * (ev.x() /self.width())
        if pos !=self.sliderPosition():
           self.setValue(int(pos))

    @property
    def margin(self):
        return self.__margin
    @margin.setter
    def margin(self,value):
        if not self.__finish:
            self.__margin=value
        else:
            raise AttributeError('不能在setStyleSheet之后设置margin')
    @property
    def setStyleSheet(self,**kwargs):
        super().setStyleSheet(self.__qss)
        return True

    @setStyleSheet.setter
    def setStyleSheet(self,value):
        self.__margin=value
        self.setStyleSheet
    @property
    def get_min(self):
        return min(self.width(),self.height())
    @property
    def get_sub_color(self):
        if hasattr(self,'sub_color'):
            return self.sub_color.name()
        else:
            return QColor('blue').name()

    @property
    def get_add_color(self):
        if hasattr(self, 'add_color'):
            return self.add_color.name()
        else:
            return QColor('white').name()

    @property
    def get_handle_color(self):
        if hasattr(self,'handle_color'):
            return self.handle_color.name()
        else:
            return QColor('red').name()
    @property
    def color(self,**kwargs):
        return
    @color.setter
    def color(self,colors:tuple[tuple[int,QColor]]):
        if not self.__finish:
            if isinstance(colors,tuple):
                for color in colors:
                    if len(color)==2:
                        if isinstance(color[0],int) and isinstance(color[1],QColor):
                            self.hasColor(self.choice[color[0]],color[1])
                        else:
                            raise AttributeError(f'第一个参数：{color[0]} 或者第二个参数：{color[1]} 的类型有问题，'
                                                 f'第一个参数应为int，第二个参数为QColor')
                    else:
                        raise Exception(f'参数的长度不为2，长度为{len(color)}')
            else:
                raise AttributeError(f'{color}是{type(color).__name__}对象,不是tuple对象')
        else:
            raise AttributeError('不能在setStyleSheet之后设置颜色')
    def hasColor(self,color_name,value):
        if hasattr(self,color_name):
            pass
        else:
            setattr(self,color_name,value)
    @property
    def __qss(self):
        qss=self.model.render(
            slider_type=self.slider_type,
            height=self.height(),
            width=self.width(),
            margin=self.margin,
            handle_width=self.get_min,
            handle_color=self.get_handle_color,
            sub_color=self.get_sub_color,
            add_color=self.get_add_color,
        )
        self.__finish=True
        return qss


