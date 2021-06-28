#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 22:34
# @Author  : 辛酉
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask
from flask_login import LoginManager

from app.models.book import db

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
