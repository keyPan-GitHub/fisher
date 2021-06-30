#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   drift.py
@Time    :   2021/06/30 16:16:16
@Author  :   辛酉
@Version :   1.0
@Contact :   gongzuo7853@163.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
'''

# here put the import lib

from app.lib.enums import PendingStatus
from app.view_moder.drift import DriftCollection
from sqlalchemy.sql.expression import desc
from sqlalchemy import or_
from app.froms.book import DriftForm
from app.lib.email import send_mail
from app.models.base import db
from app.models.drift import Drift
from app.models.gift import Gift
from flask import (current_app, flash, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from . import web

__author__ = '七月'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    current_gift = Gift.query.get_or_404(gid)
    if current_gift.is_yourself_gift(current_user.id):
        flash('这本书是你自己的，不能自己向自己赠送哦')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))
    
    can = current_user.can_send_drift()
    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)
    
    form = DriftForm(request.form)
    if request.method == 'POST' and form.validate():
        save_drift(form, current_gift)
        send_mail(current_gift.user.email, '有人想要一本书','email/get_gift.html',
                  wisher=current_user,
                  gift=current_gift)
    
    gifter = current_gift.user.summary
    return render_template('drift.html',
                           gifter=gifter, user_beans=current_user.beans,form=form)

@web.route('/pending')
@login_required
def pending():
    drifts = Drift.query.filter(
        or_(Drift.requester_id==current_user.id, 
            Drift.gifter_id==current_user.id)).order_by(
                desc(Drift.create_time)).all()
            
    views = DriftCollection(drifts,current_user.id)
    return render_template('pending.html', drifts=views.data)


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    with db.auto_commit():
        drift = Drift.query.filter(Drift.id == did).first_or_404()
        drift.pending = PendingStatus.Redraw
    return redirect(url_for('web.pending'))
    


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass



def save_drift(drift_form, current_gift):
    from app.view_moder.book import BookViewModer
    with db.auto_commit():
        drift = Drift()
        # drift.message = drift_form.message.data
        drift_form.populate_obj(drift)
        drift.gift_id = current_gift.id
        drift.requester_id = current_user.id
        drift.requester_nickname = current_user.nickname
        drift.gifter_id = current_gift.user.id    
        drift.gifter_nickname = current_gift.user.nickname   
        
        book = BookViewModer(current_gift.book)
        
        drift.book_title = book.title
        drift.book_author = book.author
        drift.book_img = book.image
        drift.isbn = book.isbn
        
        current_user.beans -= 1
        db.session.add(drift)
        