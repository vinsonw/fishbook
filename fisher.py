# coding: utf-8

__author__ = 'Vinson'

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
print(id(app))

from app.web import book


if __name__ == '__main__':
    print('I am running ', id(app))
    app.run(debug=app.config['DEBUG'], port=81)

