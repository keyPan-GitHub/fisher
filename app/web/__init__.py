#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:37
# @Author  : 辛酉
# @File    : __init__.py
# @Software: PyCharm

from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import auth, book, drift, gift, main, wish

# from app.web import user
