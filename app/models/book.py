#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 23:37
# @Author  : 辛酉
# @File    : book.py
# @Software: PyCharm

from app.models.base import Base, db
from sqlalchemy import Column, Integer, String


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)  #书籍编号
    title = Column(String(50),nullable=False) #书籍名称
    author = Column(String(30),default="俠名") #作者姓名
    binding = Column(String(20))    #装帧的版本，精装or平装
    publisher = Column(String(50))  #出版社
    price = Column(String(20)) #价格
    pages = Column(Integer) #页数
    pubdate = Column(String(20)) #出版的年月
    isbn = Column(String(15),nullable=False, unique=True) #isbn变化
    summary = Column(String(1000)) # 简介
    image = Column(String(50)) # 突破


    def sample(self):
        pass









