# coding: utf-8
# 2019/6/28 18:51
import json

from flask import jsonify, request, render_template, flash

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.view_models.book import BookViewModel, BookCollection

__author__ = 'Vinson <me@vinsonwei.com>'



@web.route('/book/search')
def search():
    """
        q 代表普通关键字或者isbn
        page
        # isbn
        # isbn13, 13个0到9的数字
        # isbn10, 10个0到9数字，含有'-'
    """
    # Request Response
    # HTTP 的请求信息
    # 查询参数 POST参数 remote ip

    # q和page都要满足一定条件才能处理
    # q至少要有一个字符，有长度限制
    # page为正整数，有最大值限制

    # 验证层 的概念
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books) # 重要：jsonify把Python中的字典转换为json格式

    else:
        flash('关键字不符合要求，检查后重新输入')
        # return jsonify(form.errors)

    return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn): #isbn参数从url中获得
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


@web.route('/test')
def test():
    r = {
        'name': '',
        'age': 18
    }

    flash('hello, Vinson', category='error')
    flash('hello, Vinson', category='warning')

    return render_template('test.html', data=r)