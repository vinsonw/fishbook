# coding: utf-8
import json

from yushu_book import YuShuBook

__author__ = 'Vinson'

from flask import Flask, make_response
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q 代表普通关键字或者isbn
        page
        # isbn
        # isbn13, 13个0到9的数字
        # isbn10, 10个0到9数字，含有'-'
    """

    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result =  YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return json.dumps(result),200,{'content-type':'application/json'} #指定返回结果为json否则默认按照html解析





if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=81)
