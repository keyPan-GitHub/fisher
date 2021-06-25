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

# here put the import lib
from app.models.base import Base, db
from app.models.gift import Gift
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Wish(Base):
    id = Column(Integer, primary_key=True)  # 用户唯一标识
    user = relationship('User')  # 外键
    uid = Column(Integer, ForeignKey('user.id'))  #在user表中获取id
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)  # 礼物送出与否，默认为未送出


