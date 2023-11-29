# -*- coding: utf-8 -*-
"""
文件:UI/手写签名/spiders.py
创建者:QE
时间:2023/8/23 16:28
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
import feapder
from feapder import AirSpider
class DownLoadSpider(AirSpider):
    def __init__(self,text,font,font_color,border_color):
        super().__init__()
        self.content = None
        self.text=text
        self.font=font
        self.font_color=font_color
        self.border_color=border_color
    def download_midware(self, request):
        request.data={
            'id': self.text,
            'zhenbi': '20191123',
            'id1': self.font,
            'id2': '15',
            'id3': self.font_color,
            'id5': self.border_color,
        }
        return request
    def start_requests(self):
        url='http://www.jiqie.com/make.php?file=a&page=14'
        yield feapder.Request(url=url,download_midware=self.download_midware)
    def parse(self, request, response):
        img_link=response.re('<img src="(.*?)">',response.text)[0]
        yield feapder.Request(url=img_link,callback=self.download_jpg,download_midware=False)
    def download_jpg(self,request, response):
        self.content=response.content

if __name__ == '__main__':
    spider=Spider()
    spider.start()