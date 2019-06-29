# coding: utf-8
# 2019/6/29 21:31
from flask import Flask


__author__ = 'Vinson <me@vinsonwei.com>'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web) #这里的register_blueprint()是app对象的方法