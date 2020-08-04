#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 21:29
# @Author  : 辛酉
# @File    : my_http.py
# @Software: PyCharm
import requests


class MY_HTTP:
    """
    发送http请求
    """

    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''
