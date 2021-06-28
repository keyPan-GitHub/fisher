#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   gift.py
@Time    :   2021/06/28 16:17:32
@Author  :   辛酉
@Version :   1.0
@Contact :   gongzuo7853@163.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
'''

# here put the import lib
# from app.web.gift import my_gifts
from collections import namedtuple

from app.view_moder.book import BookViewModer

# MyGift = namedtuple('MyGift', ['id','book','wishes_count'])

class MyGifts:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list 
        
        self.gifts = self.__parse()
    
    def __parse(self):
        temp_gift = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gift.append(my_gift)
        return temp_gift
    
    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['isbn']
        r = {
            'wishes_count':count,
            'book':BookViewModer(gift.book),
            'id':gift.id
        }
        
        # my_gift = MyGift(BookViewModer(gift.id), BookViewModer(gift.book), count)
        return r
    
    
# class MyGift:
#     def __init__(self):
#         pass
    