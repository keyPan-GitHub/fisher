
from app.models.base import db
from app.models.wish import Wish
from flask import current_app, flash, redirect, url_for
from flask_login import current_user, login_required
from flask_login.utils import login_required

from . import web

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        # with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(wish)
            db.session.commit()
    else:
        flash('这本书已添加至您的赠送清单或已存在于您的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail',isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
