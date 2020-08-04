#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 21:17
# @Author  : 辛酉
# @File    : helper.py
# @Software: PyCharm


def is_isbn_or_key(word):
    """
    判断是不是isbn码
    :param word: 传进来的参数q
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
