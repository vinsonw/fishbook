# coding: utf-8
# 2019/8/3 3:06
from sqlalchemy.orm import relationship

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

__author__ = 'Vinson <me@vinsonwei.com>'


class Gift(Base):
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    isbn = Column(String(15), nullable=False)