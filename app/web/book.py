#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 21:38
# @Author  : 辛酉
# @File    : book.py
# @Software: PyCharm

from app.view_moder.trade import TradeInfo
from app.models.wish import Wish
from app.models.gift import Gift
from app.web import gift
from flask import json, jsonify,request,url_for,render_template,flash
from flask_login import current_user

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
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books, form=form)

@web.route('/book/<isbn>/detail')    
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModer(yushu_book.first)
    
    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id,isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id,isbn=isbn,
                                launched=False).first():
            has_in_wishes = True
            
    
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes_models = TradeInfo(trade_wishes)
    trade_gifts_models = TradeInfo(trade_gifts)
    return render_template('book_detail.html',
                           book=book,
                           wishes=trade_wishes_models,
                           gifts=trade_gifts_models,
                           has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes)



@web.route('/test')    
def test():
    r = {
        'name' : None,
        'age' : 18
    }
    flash('hello 辛酉')
    flash('hello jiuyue')
    return render_template('test.html',data=r)

