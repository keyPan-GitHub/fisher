#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:37
# @Author  : 辛酉
# @File    : __init__.py
# @Software: PyCharm

from flask import Blueprint
from flask.templating import render_template

web = Blueprint('web', __name__)

@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'),404

from app.web import auth, book, drift, gift, main, wish

# from app.web import user
