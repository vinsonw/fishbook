# coding: utf-8
# 2019/6/28 18:51
from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web

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
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'isbn':
            result =  YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
