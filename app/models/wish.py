#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   gift.py
@Time    :   2021/06/19 15:44:04
@Author  :   辛酉
@Version :   1.0
@Contact :   gongzuo7853@163.com
@License :   (C)Copyright 2020-2021
@Desc    :   心愿模型
'''

from app.models.base import Base, db
# here put the import lib

from app.spider.yushu_book import YuShuBook
# from app.models.gift import Gift
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, desc, func
from sqlalchemy.orm import relationship


class Wish(Base):
    id = Column(Integer, primary_key=True)  # 用户唯一标识
    user = relationship('User')  # 外键
    uid = Column(Integer, ForeignKey('user.id'))  #在user表中获取id
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)  # 礼物送出与否，默认为未送出

    @classmethod
    def get_user_wishes(cls,uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(
            desc(Wish.create_time)).all()
        return wishes
    
    @classmethod
    def get_gifts_counts(cls,isbn_list):
        """
        根据传入的一组isbn，到wish表中计算出某个礼物
        的wish心愿数量
        Args:
            isbn_list (bool): [传入的值]
        """
        from app.models.gift import Gift
        count_list = db.session.query(func.count(Gift.id),Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(
            Gift.isbn).all()
        count_lists = [{'count':w[0],'isbn':w[1]} for w in count_list]
        return count_lists

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
