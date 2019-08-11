# coding: utf-8
# 2019/8/11 10:41
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

__author__ = 'Vinson <me@vinsonwei.com>'

class RegisterForm(Form):
    email = StringField(validators=[
        DataRequired(),
        Length(8, 64),
        Email(message='电子邮箱不符合规范')
    ])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'),
        Length(6,32)
    ])
    nickname = StringField(validators=[
        DataRequired(),
        Length(
            2,
            10,
            message='昵称长度要么太短，要么太长'
        )
    ])
