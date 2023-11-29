# -*- coding: utf-8 -*-
"""
文件:1.py
创建者:QE
时间:2023/7/14 13:37
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
from faker import Faker

f=Faker('zh_CN')
for i in range(5):
    print(f.name(),f.address())
