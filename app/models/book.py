# coding: utf-8
# 2019/6/30 21:05
from app.models.base import db, Base

__author__ = 'Vinson <me@vinsonwei.com>'

from sqlalchemy import Column, Integer, String


# SqlAlchemy -> Flask_SqlAlchemy
# WTforms -> Flask_Wtforms

# Flask
# werkzeug -> flask route



# MVC M Model 只有数据 《=》 数据库设计
# ORM对象关系映射 Code first

class Book(Base): #让自定义类继承db.Model，必需
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='佚名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(Integer)
    pubdate = Column(String(20))
    pages = Column(Integer)
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))


    def sample(self):
        pass
