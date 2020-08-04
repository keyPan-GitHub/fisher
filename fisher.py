#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 20:15
# @Author  : 辛酉
# @File    : config.py
# @Software: PyCharm

from app import create_app


app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8000)
