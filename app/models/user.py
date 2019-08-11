# coding: utf-8
# 2019/8/3 3:06
from werkzeug.security import generate_password_hash

from app.models.base import db, Base

__author__ = 'Vinson <me@vinsonwei.com>'

from sqlalchemy import Column, Integer, String, Boolean, Float

class User(Base):
    # __tablename__ = 'user1' 可以通过给该变量赋值，重新制定用户表的名称
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(11), unique=True)
    _password = Column('password', String(128))
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
