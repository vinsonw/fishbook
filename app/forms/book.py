# coding: utf-8
# 2019/6/30 4:17
from wtforms.validators import Length, NumberRange, DataRequired

__author__ = 'Vinson <me@vinsonwei.com>'

from wtforms import Form, StringField, IntegerField


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
