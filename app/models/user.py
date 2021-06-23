#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2021/06/19 15:35:42
@Author  :   辛酉
@Version :   1.0
@Contact :   gongzuo7853@163.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
'''

# here put the import lib


from app.models.wish import Wish
from app.models.gift import Gift

from sqlalchemy.sql.expression import false
from app.models.base import db,Base
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import Column, String, Integer, Boolean, Float
from flask_login import UserMixin
from app import login_manager
from app.lib.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

class User(UserMixin,Base):
    id = Column(Integer, primary_key=True) # 用户唯一标识
    nickname = Column(String(24),nullable=False) # 名称
    phone_number = Column(String(18),unique=True) #手机号
    _password = Column("password", String(128),nullable=False) #加密密码
    email = Column(String(20),unique=True, nullable=False)    #邮件地址
    confirmed = Column(Boolean,default=False)  #出版社
    beans = Column(Float,default=0) #价格
    send_counter = Column(Integer, default=0) #页数
    receive_counter = Column(Integer, default=0) #出版的年月
    wx_open_id = Column(String(50)) #isbn变化
    wx_name = Column(String(32)) # 简介

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self,raw):
        return check_password_hash(self._password,raw)
    
    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 不允许一个用户同时赠送多本相同的图书
        # 一个用户不可能同时成为赠送者和索要者
        
        # 这本图书，必须既不在赠送清单、也不再心愿清单。
        gifting = Gift.query.filter_by(uid=self.id,isbn=isbn,
                                       launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id,isbn=isbn,
                                       launched=False).first()
        
        if not gifting and not wishing:
            return True
        else:
            return False
        
    # def get_id(self):
    #     return self.id

    
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))