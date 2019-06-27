# coding: utf-8
__author__ = 'Vinson'

from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q 代表普通关键字或者isbn
        page
    """
    # isbn
    # isbn13, 13个0到9的数字
    # isbn10, 10个0到9数字，含有'-'
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'



if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=81)
