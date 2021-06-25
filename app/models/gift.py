#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   gift.py
@Time    :   2021/06/19 15:44:04
@Author  :   辛酉
@Version :   1.0
@Contact :   gongzuo7853@163.com
@License :   (C)Copyright 2020-2021
@Desc    :   礼物模型
'''

# here put the import lib
from app.models.base import Base, db
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,desc
from sqlalchemy.orm import relationship
from flask import current_app

from app.spider.yushu_book import YuShuBook

class Gift(Base):
    id = Column(Integer, primary_key=True) # 用户唯一标识
    user = relationship('User')  # 外键
    uid = Column(Integer, ForeignKey('user.id')) #在user表中获取id
    isbn = Column(String(15),nullable=False) 
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean,default=False) # 礼物送出与否，默认为未送出
    
    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
    
    @classmethod
    # @property
    def recent(cls):
        recent_gifts = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gifts
    
       
