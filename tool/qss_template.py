# -*- coding: utf-8 -*-
"""
文件:qss_template.py
创建者:QE
时间:2023/8/11 18:16
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
from jinja2 import Template, FileSystemLoader, Environment, PackageLoader


class QssTemplate:
    def __init__(self, path: object):
        __loader = PackageLoader('qss', 'Templates')
        __env = Environment(loader=__loader)
        self.template = __env.get_template(path)

    def render(self, **kwargs):
        return self.template.render(**kwargs)
