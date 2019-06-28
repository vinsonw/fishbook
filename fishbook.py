# coding: utf-8
import json

from yushu_book import YuShuBook

__author__ = 'Vinson'

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app.web import book


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=81)
