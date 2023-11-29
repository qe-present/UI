# -*- coding: utf-8 -*-
"""
文件：UI/mysql/base.py
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
import pymysql
from pymysql.err import OperationalError,ProgrammingError
from tool.logger import logger
from prettytable import PrettyTable
from .settings import *
class Base:
    def __init__(self):
        self.connect = pymysql.connect(host=host, user=user, password=password, port=port)
        self.cursor = self.connect.cursor()
        self.log = logger
    def _init_table(self,title:list[str],rows:list):
        table=PrettyTable()
        table.field_names = title
        table.add_rows(
            rows
        )
        return table
    def __close(self):
        self.connect.close()
        self.cursor.close()

    def __enter__(self):
        self.log.info('连接数据库成功')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log.info('关闭数据库')
        self.__close()
    def __commit(self):
        self.connect.commit()

    def __sql(self, query: str, args=None, many: bool = None):
        """
        :param sql:  sql 语句
        :arg: 参数
        :return: None
        """
        if many:
            self.cursor.executemany(query=query, args=args)
        else:
            self.cursor.execute(query=query, args=args)
        self.__commit()

    def sql(self, query, args=None,many=None):
        self.log.info(f'执行sql语句：{query}')
        self.__sql(query=query, args=args, many=many)
        return self.__result()
    def __result(self):
        try:
            result=self.cursor.fetchall()
            if result:
                return list(map(list,result))
            else:
                None
        except ProgrammingError as e:
            self.log.debug(e)
    def db(self, db_name):
        query=f'use {db_name};'
        self.__sql(query)
        self.log.info(f'使用数据库为{self.now_db}')
        return self
    @property
    def now_db(self):
        return self.sql('select database()')[0][0]


