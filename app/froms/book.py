#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 16:30
# @Author  : 辛酉
# @File    : book.py
# @Software: PyCharm

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange


class SearchFrom(Form):
    q = StringField(validators=[Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)








