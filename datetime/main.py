# -*- coding: utf-8 -*-
"""
文件:main.py
创建者:QE
时间:2023/7/21 15:09
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
from pyDes import des, CBC, PAD_PKCS5
from dataclasses import dataclass
import binascii
import sys
from times import Ui_Form

from random import sample
from datetime import datetime,date
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
class Main(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__initui()
    def __initui(self):
        date=QDate.currentDate()
        self.key.setDate(date)
        timer=QTimer(self)
        timer.start(2000)
        timer.timeout.connect(self.ok)

    def ok(self):
        now_datatime=QDateTime.currentDateTime()
        self.data_ming.setDateTime(now_datatime)

    @pyqtSlot(QDateTime)
    def on_data_ming_dateTimeChanged(self,now_datatime):
        now=now_datatime.toPyDateTime()
        tt=str(int(now.timestamp()*1000))
        key=self.key.date().toPyDate().strftime('%Y%m%d')
        plaintext=tt+''.join(map(str,sample(range(1,10),5)))
        d = Des(plaintext, key)
        ciphertext= d.des_encrypy()
        plain_text= d.des_decrypy(ciphertext)
        self.time_tt.setText(f'时间戳:{tt}')
        self.plaintext.setText(f'明文:{plaintext}')
        self.ciphertext.setText(f'密文:{ciphertext}')
        self.end_time.setText(f'解密的时间:{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(plain_text[:-5]) /1000))}')
"""
:key
data
mode
"""
@dataclass
class Des:
    data:str
    key:str
    def des_encrypy(self):
        iv = self.key
        k = des(self.key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        mi = k.encrypt(self.data, padmode=PAD_PKCS5)
        # binascii.b2a_hex 将输入a转为2进制并以16进制显示返回b
        return binascii.b2a_hex(mi).decode()
    def des_decrypy(self,miwen):
        iv = self.key
        k = des(self.key, CBC,iv, pad=None, padmode=PAD_PKCS5)
        ming :bytes= k.decrypt(binascii.a2b_hex(miwen), padmode=PAD_PKCS5)
        return ming.decode('utf-8')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    h=Main()
    h.show()
    sys.exit(app.exec_())