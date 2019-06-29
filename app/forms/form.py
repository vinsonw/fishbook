# coding: utf-8
# 2019/6/30 4:17
from wtforms.validators import Length

__author__ = 'Vinson <me@vinsonwei.com>'

from wtforms import Form, StringField


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30)])