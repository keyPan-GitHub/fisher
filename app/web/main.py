from app.models.gift import Gift
from app.view_moder.book import BookViewModer
from flask import render_template

from . import web

__author__ = '七月'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModer(gift.book) for gift in recent_gifts]
    return render_template('index.html',rencent=books)


@web.route('/personal')
def personal_center():
    pass
