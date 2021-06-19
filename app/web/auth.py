#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   auth.py
@Time    :   2021/06/19 16:41:48
@Author  :   辛酉
@Version :   1.0
@Contact :   gongzuo7853@163.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
'''

# here put the import lib

from . import web
from flask.templating import render_template


__author__ = '七月'


@web.route('/register',methods=['GET','POST'])
def register():
    return render_template('auth/register.html',form={'data':{}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
