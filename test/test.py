# coding: utf-8
# 2019/7/2 0:04

__author__ = 'Vinson <me@vinsonwei.com>'

from flask import Flask, current_app, request, Request

app = Flask(__name__)

# flask中的上下文
# 应用上下文 对象 对Flask对象的的封装
# 请求上下文 对象 对Request对象的封装
# Flask存储在AppContext对象中
# Request存储在RequestContext对象中
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

with app.app_context():
    a = current_app
    print('a = ', a)
    d = current_app.config['DEBUG']
    a = 1
    print('d = ', d)



# 实现了上下文协议(也就是实现了__enter__和__exit__方法)的对象使用with
# 这样的对象称为上下文管理器
# 上下文表达式（app.app_context()）必须返回一个上下文管理器



# class Foo:
#     def __enter__(self):
#         a = 1
#         return a
#     def __exit__(self, exc_type, exc_value, tb):
#         b = 1
# with Foo() as obj_Foo:
#     pass

class MyResource:
    def __enter__(self):
        print('Connecting to resources.')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('process exception now')
        else:
            print('no exception')
        print('Closing resources connection')
        return False # 如果返回True，则异常不在外抛
    def query(self):
        print('Querying')

try:
    with MyResource() as resource:
        1/0
        resource.query()
except Exception as ex:
    pass

