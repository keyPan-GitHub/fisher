#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 21:38
# @Author  : 辛酉
# @File    : book.py
# @Software: PyCharm
from flask import jsonify,request
from app.froms.book import SearchFrom
from . import web

from app.lib.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


# 蓝图


@web.route('/book/search')
def search():
    """
    当前函数要接收，q,start,count,isbn四个参数
    :return:
    """
    form = SearchFrom(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify({'msg:参数校验失败'})
