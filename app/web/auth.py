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

from app.froms.auth import (EmailForm, LoginForm, RegisterForm,
                            ResetPasswordForm)
# here put the import lib
from app.lib.email import send_mail
from app.models.base import db
from app.models.user import User
from flask import redirect, render_template, request, url_for
from flask.helpers import flash
from flask_login import login_user, logout_user

from . import web

__author__ = '七月'


@web.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        # with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
            db.session.commit() 
            return redirect(url_for('web.login'))

    return render_template('auth/register.html',form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next =  request.args.get('next')
            if not next or not next.startswith('/'): 
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在，或密码错误')
    return render_template('auth/login.html', form=form)



@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()
            
            send_mail(form.email.data,'重置你的密码', 
                      'email/reset_password.html', user=user, 
                       token=user.generate_token())
            flash('一封邮件已发送到邮箱'+account_email+',请及时查收')
            # return redirect(url_for('web.login'))
    return render_template('auth/forget_password_request.html',form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm()
    if request.method == 'POST' and form.validate():
        success = User.reset_password(token,form.password1.data)
        if success:
            flash('您的密码已更新，请使用新密码登录')
            return redirect(url_for('web.login'))
        else:
            flash('密码重置失败')
    return render_template('auth/forget_password.html',form=form)



@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))
    
