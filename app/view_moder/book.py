#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   book.py
@Time    :   2021/04/27 20:26:08
@Author  :   辛酉
@Version :   1.0
@Contact :   gongzuo7853@163.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
'''

# here put the import lib

from app.web import book

class BookViewModer:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.isbn = book['isbn']
        self.pages = book['pages']
        self.pubdate = book['pubdate']
        self.binding = book['binding']
    
    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author,self.publisher,self.price])
        return ' /'.join(intros)
    
class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book,keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModer(book) for book in yushu_book.books]


class _BookViewModer:
    @classmethod
    def package_singe(cls,data,keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword,
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned
        
    @classmethod
    def package_collection(cls,data,keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword,
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned
        
    @classmethod
    def __cut_book_data(cls,data):
        book = {
            'title':data['title'],
            'publisher':data['publisher'],
            'pages':data['pages'] or '',
            'author':'、'.join(data['author']),
            'price':data['price'],
            'summary':data['summary'] or '',
            'image':data['image']
        }
        return book

