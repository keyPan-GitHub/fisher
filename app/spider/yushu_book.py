#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 20:06
# @Author  : 辛酉
# @File    : yushu_book.py
# @Software: PyCharm
from app.lib.my_http import MY_HTTP


class YuShuBook:
    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&start={}&count={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = MY_HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        result = MY_HTTP.get(url)
        return result
