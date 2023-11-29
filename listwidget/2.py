# -*- coding: utf-8 -*-
"""
文件:2.py
创建者:QE
时间:2023/8/6 14:44
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
# -*- coding: utf-8 -*-
"""
文件:main.py
创建者:QE
时间:2023/7/31 14:55
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
from listwidget import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from qt_material import apply_stylesheet
from  load_main import Download
class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.duration = None
        self.h = None
        self.setupUi(self)
        self.path="C:/Users/520/Music"
        self.player=QMediaPlayer()
        self.player.durationChanged.connect(self.get_time)
        self.__initui()
    def __initui(self):
        self.__init_widget()
    def __init_widget(self):
        dir=QDir(self.path)
        mp3_data=dir.entryList(['*.mp3'])
        self.listWidget.addItems(mp3_data)
    def update_listwidegt(self):
        self.listWidget.clear()
        self.__init_widget()
    @pyqtSlot()
    def on_dele_clicked(self):
        item=self.listWidget.currentItem()
        self.listWidget.takeItem(self.listWidget.row(item))
    @pyqtSlot(QListWidgetItem)
    def on_listWidget_itemDoubleClicked(self,item):
        self.start_music(item)
    def start_music(self,item):
        content=item.data(0)
        row=self.listWidget.row(item)
        mp3_path=self.path+'/'+content
        url=QUrl.fromLocalFile(mp3_path)
        media=QMediaContent(url)
        self.player.setMedia(media)
        self.player.play()
        self.music_name.setText(f'{content}')
        self.music_name.adjustSize()
        self.listWidget.setCurrentRow(row)
    def get_time(self,duration):
        duration /= 60000
        self.duration=round(duration,5)


    @pyqtSlot()
    def on_download_clicked(self):
        self.d=Download()
        accept=self.d.exec_()
        if accept:
            self.update_listwidegt()
    @pyqtSlot()
    def on_next_music_clicked(self):
        row=self.listWidget.currentRow()
        if row==self.listWidget.count()-1:
            new_row=0
        else:
            new_row=row+1
        item=self.listWidget.item(new_row)
        self.start_music(item)

    @pyqtSlot()
    def on_previous_music_clicked(self):
        row=self.listWidget.currentRow()
        if row==0:
            new_row=self.listWidget.count()-1
        else:
            new_row=row-1
        item=self.listWidget.item(new_row)
        self.start_music(item)
    @pyqtSlot()
    def on_play_music_clicked(self):
        item=self.listWidget.currentItem()
        self.start_music(item)
    @pyqtSlot()
    def on_pause_play_clicked(self):
        state=self.player.state()
        if state==self.player.PlayingState:
            self.player.pause()
        elif state==self.player.PausedState|self.player.StoppedState:
            self.player.play()
    @pyqtSlot()
    def on_stop_music_clicked(self):
        self.player.stop()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())