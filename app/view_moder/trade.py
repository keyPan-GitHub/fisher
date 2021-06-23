#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   trade.py
@Time    :   2021/06/23 14:30:19
@Author  :   辛酉
@Version :   1.0
@Contact :   gongzuo7853@163.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
'''

# here put the import lib

from time import strftime

class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self._parse(goods)
    
    def _parse(self, goods):
        self.total = len(goods)
        self.trades = [self._map_to_trade(single) for single in goods]

    def _map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d'),
        else:
            time = "未知"
        return dict(
            user_name = single.user.nickname,
            time = time,
            id = single.id
        )