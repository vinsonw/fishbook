# coding: utf-8
# 2019/7/8 0:24

__author__ = 'Vinson <me@vinsonwei.com>'

from werkzeug.local import LocalStack

# push, pop, top

s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)
