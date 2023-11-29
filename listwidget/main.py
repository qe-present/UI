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
import logging
import sys
from listwidget import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from  load_main import Download
class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.now_volumn=40
        self.horizontalSlider.setEnabled(False)
        self.setAcceptDrops(True)
        self.play_slider.setStyleSheet
        self.play_slider.setEnabled(False)
        self.duration = None
        self.h = None
        self.path="C:/Users/520/Music"
        self.player=QMediaPlayer()
        self.player.durationChanged.connect(self.get_time)
        self.__initui()
    def __initui(self):
        self.timer=QTimer(self,timeout=self.times)
        self.__init_widget()
    def times(self):
        if self.play_slider.value()==self.play_slider.maximum():
            self.timer.stop()
            return
        self.play_slider.setValue(self.play_slider.value()+1)
    def __init_widget(self):
        dir=QDir(self.path)
        mp3_data=dir.entryList(['*.mp3'])
        self.listWidget.addItems(mp3_data)

    def update_listwidegt(self):
        self.listWidget.clear()
        self.__init_widget()

    def get_time(self,duration):
        all_sec=int(duration/1000)
        minute,second=divmod(all_sec,60)
        self.play_slider.setRange(0,all_sec)
    def start_muisc(self, item):
        self.horizontalSlider.setEnabled(True)
        self.play_slider.setEnabled(True)
        self.timer.start(1000)
        content = item.data(0)
        mp3_path = self.path + '/' + content
        url = QUrl.fromLocalFile(mp3_path)
        media = QMediaContent(url)
        self.player.setMedia(media)
        self.player.play()
        self.player.setVolume(self.now_volumn)
        self.horizontalSlider.setValue(self.now_volumn)
        self.listWidget.setCurrentItem(item)
        self.music_name.setText(f'{content}')
        self.music_name.adjustSize()
    @pyqtSlot(int)
    def on_horizontalSlider_valueChanged(self,tick):
        self.now_volumn=tick
        self.player.setVolume(tick)
    @pyqtSlot(int,int)
    def on_play_slider_valueChanged(self,tick,_):
        self.player.setPosition(tick*1000)
    @pyqtSlot()
    def on_dele_clicked(self):
        item=self.listWidget.currentItem()
        self.listWidget.takeItem(self.listWidget.row(item))
    @pyqtSlot(QListWidgetItem)
    def on_listWidget_itemDoubleClicked(self,item):
        self.start_muisc(item)
    @pyqtSlot()
    def on_download_clicked(self):
        self.d=Download()
        self.d.show()
    @pyqtSlot()
    def on_next_music_clicked(self):
        row=self.listWidget.currentRow()
        if row==self.listWidget.count()-1:
            row=0
        else:
            row+=1
        item=self.listWidget.item(row)
        self.start_muisc(item)
    @pyqtSlot()
    def on_previous_music_clicked(self):
        row=self.listWidget.currentRow()
        if row==0:
            row=self.listWidget.count()-1
        else:
            row-=1
        item=self.listWidget.item(row)
        self.start_muisc(item)
    @pyqtSlot()
    def on_play_pause_clicked(self):
        state=self.player.state()
        print(state)
        if state==QMediaPlayer.StoppedState:
            item=self.listWidget.currentItem()
            self.start_muisc(item)
            self.play_pause.setIcon(QIcon(':/暂停.png'))
            self.timer.start(1000)
        elif state==QMediaPlayer.PausedState:
            self.player.play()
            self.play_pause.setIcon(QIcon(':/暂停.png'))
            self.timer.stop()
        else:
            self.player.pause()
            self.play_pause.setIcon(QIcon(':/播放.png'))
            self.timer.stop()
    def closeEvent(self, a0: QCloseEvent) -> None:
        self.player.stop()
        print('关闭音乐')
    def dragEnterEvent(self, a0: QDragEnterEvent) -> None:
        self.drag_data:QMimeData=a0.mimeData()
        if self.drag_data.hasText():
            a0.accept()
        else:
            a0.ignore()
    def dropEvent(self, a0: QDropEvent) -> None:
        index=int(self.drag_data.text())
        Download.drag_music(self.d,index)
        self.update_listwidegt()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())