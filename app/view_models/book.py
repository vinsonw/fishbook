# coding: utf-8
# 2019/7/13 20:36

__author__ = 'Vinson <me@vinsonwei.com>'

# view model是对从数据库或者API取回的data做一层wrap，以便满足数据展示的需要

class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword): # 将单本书的数据转换为查询关键字只有一个本的情形
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data): # 裁剪数据
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'],
            'image':data['image']
        }
        return book
