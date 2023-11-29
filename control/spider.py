# -*- coding: utf-8 -*-
"""
文件:UI/control/spider.py
创建者:QE
时间:2023/8/24 16:14
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
class Spider(AirSpider):
    def __init__(self,url):
        super().__init__()
        self.url=url
        self.font_list=None
    def start_requests(self):
        yield feapder.Request(url=self.url)
    def parse(self, request, response):
        option_sel=response.xpath('//*[@id="id1"]/option')
        font_list=[]
        for i in option_sel:
            key=i.xpath('./text()').get()
            value=i.xpath('./@value').get()
            a={key:value}
            font_list.append(a)
        self.font_list=font_list
