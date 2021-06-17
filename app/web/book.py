#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 21:38
# @Author  : 辛酉
# @File    : book.py
# @Software: PyCharm

from flask import json, jsonify,request,url_for,render_template,flash

from . import web
from app.lib.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.froms.book import SearchFrom

from app.view_moder.book import BookCollection, BookViewModer




# 蓝图


@web.route('/book/search')
def search():
    """
    当前函数要接收，q,start,count,isbn四个参数
    :return:
    """
    form = SearchFrom(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q,page)
        books.fill(yushu_book,q)
        return json.dumps(books,default=lambda o:o.__dict__)
    else:
        return jsonify(form.errors)

@web.route('/test')    
def test():
    r = {
        'name' : None,
        'age' : 18
    }
    flash('hello 辛酉')
    flash('hello jiuyue')
    return render_template('test.html',data=r)

