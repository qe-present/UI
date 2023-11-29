# -*- coding: utf-8 -*-
"""
文件:UI/手写签名/spider.py
创建者:QE
时间:2023/8/23 16:04
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
    def start_requests(self):
        url='http://www.jiqie.com/a/15.htm'
        yield feapder.Request(url=url)
    def parse(self, request, response):
        option_sel=response.xpath('//*[@id="id1"]/option')
        font_list=[]
        for i in option_sel:
            key=i.xpath('./text()').get()
            value=i.xpath('./@value').get()
            a={key:value}
            font_list.append(a)




if __name__ == '__main__':
    spider=Spider()
    spider.start()