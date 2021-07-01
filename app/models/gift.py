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


from collections import namedtuple

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook
from flask import current_app
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, desc, func
from sqlalchemy.orm import relationship


class Gift(Base):
    id = Column(Integer, primary_key=True) # 用户唯一标识
    user = relationship('User')  # 外键
    uid = Column(Integer, ForeignKey('user.id')) #在user表中获取id
    isbn = Column(String(15),nullable=False) 
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean,default=False) # 礼物送出与否，默认为未送出
    
    def is_yourself_gift(self, uid):
        return True if self.uid == uid else False
    
    @classmethod
    def get_user_gift(cls,uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts
    
    @classmethod
    def get_wish_counts(cls,isbn_list):
        """
        根据传入的一组isbn，到wish表中计算出某个礼物
        的wish心愿数量
        Args:
            isbn_list (bool): [传入的值]
        """
        from app.models.wish import Wish
        count_list = db.session.query(func.count(Wish.id),Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(
            Wish.isbn).all()
        count_lists = [{'count':w[0],'isbn':w[1]} for w in count_list]
        return count_lists
    
    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
    
    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
    
    
