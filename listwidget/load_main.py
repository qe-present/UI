# -*- coding: utf-8 -*-
"""
文件:load_main.py
创建者:QE
时间:2023/8/2 14:03
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
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from faker import Faker
from download import Ui_Form


class Download(QDialog, Ui_Form):
    s=None
    def __init__(self):
        super().__init__()
        self.s = None
        self.data = None
        self.setupUi(self)
        self.path = 'C:/Users/520/Music/'
        self.title = ['歌名', '专辑', '歌手']
        self.model = QStandardItemModel(self)
        self.__initui()

    def __initui(self):
        self.setWindowTitle('下载歌曲')
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.customContextMenuRequested.connect(self.rightkey)
        self.tableView.setDragEnabled(True)

    def rightkey(self, pos):
        menu = QMenu()
        dowmload = menu.addAction('下载')
        loser = menu.addAction('关闭')
        action = menu.exec_(self.tableView.mapToGlobal(pos))
        if action == dowmload:
            model = self.tableView.selectionModel()
            if model:
                rows = model.selectedRows()
                for i in rows:
                    index = i.row()
                    index = 19 - index

                    Download.drag_music(self,index)

        if action == loser:
            self.accept()
    @staticmethod
    def drag_music(self,index):
        ok, msg = self.s.get_music(index)
        if not ok:
            QMessageBox.information(self, '下载失败', msg)
        else:
            self.download_mp3(msg, index)



    def download_mp3(self, response, index):
        name = self.data[0][index][0]
        total = int(response.headers['Content-Length'])
        self.bar = QProgressDialog(f'下载音乐-{name}', '取消', 0, total, self)
        self.bar.show()
        path = self.path + f'{name}.mp3'
        num=0
        with open(path, 'wb') as f:
            for i in response.iter_content(1024):
                f.write(i)
                num+=len(i)
                self.bar.setValue(num)
                QApplication.processEvents()

    @pyqtSlot()
    def on_search_clicked(self):
        self.model.setRowCount(0)
        key = self.lineEdit.text()
        pn = self.page.value()
        rn = self.total.value()
        if key:
            self.s = Spider(key, pn, rn)
            self.data = self.s.get_all_data()
            self.tableView.DATA=self.data
            if self.data:
                self.__init_title()
                self.__init_content()

    def __init_title(self):
        for i, t in enumerate(self.title):
            self.model.setHorizontalHeaderItem(i, QStandardItem(t))
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def __init_content(self):
        row = self.model.rowCount()
        for t in self.data[0]:
            self.model.insertRow(row)
            for col, text in enumerate(t):
                self.model.setItem(row, col, QStandardItem(text))
            row + 1


class Spider:
    def __init__(self, key, pn=1, rn=20):
        self.url = f'https://kuwo.cn/api/www/search/searchMusicBykeyWord?key={key}&pn={pn}&rn={rn}'
        self.headers = {
            'User-Agent': Faker().user_agent(),
            'Cookie': 'Hm_Iuvt_cdb524f42f0ce19b169b8072123a4727=piZMMJRpFPYxxa8TaHTCBhmYGe2rZswr; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1690948881,1690963839,1691042390,1692167469; _ga=GA1.2.1494005685.1692167469; _gid=GA1.2.1545721550.1692167469; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1692173069; _ga_ETPBRPM9ML=GS1.2.1692173032.2.1.1692173069.23.0.0; Hm_Iuvt_cdb524f42f0cer9b268e4v7y734w5esq24=2T8KsMFa8tx6DhBf5aQkAtwYawR8n6rK',
            'Host': 'kuwo.cn',
            'Referer': 'https://kuwo.cn/search/list',
            'Secret': '12ed27808ab6620b4384aa66adf14dcd2f806d7476130615a2325dab44c01a2403b606b4'
        }
        self.data = []
        self.rid = []

    def get_all_data(self):
        r = requests.get(url=self.url, headers=self.headers)
        try:
            json_data = r.json()
            all_music = json_data['data']['list']
            for i in all_music:
                album = i['album'].replace('&nbsp;', " ").replace("&apos;", "'")
                name = i['name'].replace('&nbsp;', " ")
                artist = i['artist']
                rid = i['rid']
                self.data.append([name, album, artist])
                self.rid.append(rid)
            self.data.reverse()
            self.rid.reverse()
            return self.data, self.rid
        except Exception as e:
            print(e)

    def get_music(self, index: int):
        rid = self.rid[index]
        get_mp3_url = f'https://kuwo.cn/api/v1/www/music/playUrl?mid={rid}&type=music'
        resp = requests.get(url=get_mp3_url, stream=True, headers=self.headers)
        mp3_json = resp.json()
        if mp3_json['code'] == 200:
            mp3_url = mp3_json['data']['url']
            r = requests.get(url=mp3_url, stream=True)
            return True, r
        else:
            return False, mp3_json['msg']


if __name__ == '__main__':
    app = QApplication(sys.argv)
    h = Download()
    h.show()
    sys.exit(app.exec_())
