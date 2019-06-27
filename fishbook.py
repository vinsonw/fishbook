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


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=81)
