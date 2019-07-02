# coding: utf-8
# 2019/6/29 21:31
from flask import Flask
from app.models.book import db

__author__ = 'Vinson <me@vinsonwei.com>'

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)

    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web) #这里的register_blueprint()是app对象的方法