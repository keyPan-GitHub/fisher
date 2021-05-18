#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:34
# @Author  : 辛酉
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask
from app.models.book import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
