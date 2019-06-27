# coding: utf-8
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





if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=81)
