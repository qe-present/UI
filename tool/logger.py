# -*- coding: utf-8 -*-
"""
文件：UI/utils/logger.py
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
from logging import getLogger, StreamHandler, DEBUG
from colorlog import ColoredFormatter
class Log:
    def __init__(self):
        self.__logger = getLogger(__file__)
        self.__stream_handler = StreamHandler()

    @property
    def set(self):
        """
        日志的配置
        :return:
        """
        colors = {
            'DEBUG': 'bold_red',
            'INFO': 'bold_blue',
            'WARNING': 'bold_yellow',
        }
        self.__logger.setLevel(DEBUG)
        color_formatter = ColoredFormatter(
            fmt='%(log_color)s'
                '%(asctime)s | '
                '%(filename)s | '
                '%(module)s.%(funcName)s line:%(lineno)d %(levelname)s : %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            log_colors=colors
        )
        self.__stream_handler.setFormatter(color_formatter)
        self.__logger.addHandler(self.__stream_handler)
        return self.__logger
logger = Log().set
