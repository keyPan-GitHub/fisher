#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 21:15
# @Author  : 辛酉
# @File    : config.py
# @Software: VScode

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:12345678@localhost:3306/fisher'
SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'

# Email 配置
MAIL_SERVER = 'smtp.qq.com'  
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'pxy1010995752@vip.qq.com'
MAIL_PASSWORD = 'xbofhiuknaiibehj'
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <hello@yushu.im>'


# 开启数据库查询性能测试
# SQLALCHEMY_RECORD_QUERIES = True

# # 性能测试的阀值
# DATABASE_QUERY_TIMEOUT = 0.5

# SQLALCHEMY_TRACK_MODIFICATIONS = True

# WTF_CSRF_CHECK_DEFAULT = False

# SQLALCHEMY_ECHO = True

# from datetime import timedelta
# REMEMBER_COOKIE_DURATION = timedelta(days=30)

# PROXY_API = 'http://ip.yushu.im/get'

# # PERMANENT_SESSION_LIFETIME = 3600