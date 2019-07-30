# coding: utf-8
# 2019/6/29 21:36
from flask import Blueprint

__author__ = 'Vinson <me@vinsonwei.com>'

web = Blueprint('web', __name__)

from app.web import book, auth, book, drift, gift, main, test, wish
from app.web import user


