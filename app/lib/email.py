#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   email.py
@Time    :   2021/06/29 16:13:07
@Author  :   辛酉
@Version :   1.0
@Contact :   gongzuo7853@163.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
'''

from threading import Thread 
from app import mail
from flask_mail import Message
from flask  import current_app,app,render_template

# here put the import lib

def send_aync_mail(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件',sender='aaa@qq.com',body='Test',
    #               recipients=['user@ qq.com'])
    msg = Message('[鱼书]'+ ' ' + subject, 
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    thr = Thread(target=send_aync_mail,args=[current_app, msg])
    thr.start()
