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

from sqlalchemy.sql.expression import true
from app.models.base import Base, db

from sqlalchemy import Column, String, Integer, Boolean, Float

class User(db.Model):
    id = Column(Integer, primary_key=True) # 用户唯一标识
    nickname = Column(String(24),nullable=False) # 名称
    phone_number = Column(String(18),unique=True) #手机号
    email = Column(String(20),unique=True, nullable=False)    #邮件地址
    confirmed = Column(Boolean,default=False)  #出版社
    beans = Column(Float,default=0) #价格
    send_counter = Column(Integer, default=0) #页数
    receive_counter = Column(Integer, default=0) #出版的年月
    wx_open_id = Column(String(50)) #isbn变化
    wx_name = Column(String(32)) # 简介