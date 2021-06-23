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

from . import web
from app.models.gift import Gift
from app.models.base import db
from flask import current_app,redirect
from flask_login import login_required,current_user
from flask.helpers import flash, url_for


__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


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



