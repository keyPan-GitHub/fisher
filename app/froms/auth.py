#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   auth.py
@Time    :   2021/06/19 16:56:59
@Author  :   辛酉
@Version :   1.0
@Contact :   gongzuo7853@163.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
'''

# here put the import lib

from wtforms import Form, IntegerField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, Length, NumberRange, ValidationError
from app.models.user import User

class RegisterForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),
                                    Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入密码'),Length(6,32)])

    nickname = StringField(validators=[DataRequired(),Length(2,10,message='昵称字少需要两个字符，最多10个字符')])
    
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self,field): 
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被注册')

class LoginForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),
                                    Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入密码'),Length(6,32)])