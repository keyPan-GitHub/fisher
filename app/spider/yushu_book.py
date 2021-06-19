#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 20:06
# @Author  : 辛酉
# @File    : yushu_book.py
# @Software: PyCharm
from app.lib.my_http import MY_HTTP
from flask import current_app

class YuShuBook:
    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'
    
    def __init__(self):
        self.total = 0
        self.books = []
    
    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = MY_HTTP.get(url)
        self.__fill_single(result)
        
    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_Collection(self, data):
        self.total = data['total']
        self.books = data['books']

    
    def search_by_keyword(self, keyword, page=2):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], 
                                    self.calculate_start(page))
        result = MY_HTTP.get(url)
        self.__fill_Collection(result)

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']


    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
