# coding: utf-8
# 2019/8/3 3:06
from sqlalchemy import Column, Integer, SmallInteger

__author__ = 'Vinson <me@vinsonwei.com>'

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    # create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)