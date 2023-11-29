# -*- coding: utf-8 -*-
"""
文件：UI/mysql/page.py
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
from .base import Base
from prettytable import PrettyTable
class Page(Base):
    def __init__(self):
        super().__init__()
    def get_word(self,table_name,show=False):
        result=self.sql(f'select column_name from information_schema.columns where table_name="{table_name}"')
        if show:
            table = self._init_table(['column_name'],result)
            return table,self
        else:
            return result,self
    def display(self):
        pass


