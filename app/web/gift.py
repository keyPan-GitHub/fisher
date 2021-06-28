#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   gift.py
@Time    :   2021/06/23 13:40:43
@Author  :   辛酉
@Version :   1.0
@Contact :   gongzuo7853@163.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
'''

# here put the import lib

from app.models.base import db
from app.models.gift import Gift
from app.view_moder.gift import MyGifts
from flask import current_app, redirect, render_template
from flask.helpers import flash, url_for
from flask_login import current_user, login_required

from . import web

__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gift(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyGifts(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html',gifts=view_model.gifts)


@web.route('/gifts/book/<isbn>')
@login_required 
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        try:
        # with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    else:
        flash('这本书已添加至您的赠送清单或已存在于您的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail',isbn=isbn))
    


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



