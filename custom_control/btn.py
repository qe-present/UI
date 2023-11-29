# -*- coding: utf-8 -*-
"""
文件：UI/custom_control/btn.py
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
from PyQt5.QtDesigner import QDesignerCustomWidgetInterface
from custom_btn import MyCustomButton
class MyCustomButtonPlugin(QDesignerCustomWidgetInterface):
    def __init__(self):
        super().__init__()
        self.initialized = False

    def initialize(self, formEditor):
        if self.initialized:
            return
        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return MyCustomButton(parent)

    def name(self):
        return "MyCustomButton"

    def group(self):
        return "Custom Widgets"

    def icon(self):
        # 返回插件的图标
        return QIcon('播放.png')

    def toolTip(self):
        return "My Custom Button"

    def whatsThis(self):
        return "This is a custom button."

    def isContainer(self):
        return False

    def domXml(self):
        # 返回插件的XML描述
        return """
        <widget class="CustomWidget" name="customWidget">
                <property name="toolTip" >
                <string>A custom widget plugin</string>
                 </property>
                 <property name="whatsThis" >
                 <string>A custom widget plugin.</string>
                 </property>
               </widget>
        """

    def includeFile(self):
        return "custom_control"

