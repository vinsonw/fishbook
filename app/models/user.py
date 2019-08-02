# coding: utf-8
# 2019/8/3 3:06
from app.models.base import db

__author__ = 'Vinson <me@vinsonwei.com>'

from sqlalchemy import Column, Integer, String, Boolean, Float

class User(db.Model):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(11), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
