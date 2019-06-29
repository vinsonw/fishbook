# coding: utf-8
# 2019/6/28 18:51
from flask import jsonify, request

from helper import is_isbn_or_key
from yushu_book import YuShuBook
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

    q = request.args['q']
    page = request.args['page']

    # 验证q




    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result =  YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # return json.dumps(result),200,{'content-type':'application/json'} #指定返回结果为json否则默认按照html解析
