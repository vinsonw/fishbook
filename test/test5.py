# coding: utf-8
# 2019/7/7 21:38
import threading
import time

from werkzeug.local import Local

__author__ = 'Vinson <me@vinsonwei.com>'

# 线程隔离对象Local

# werkzeug local Local 实现线程
# Local使用字典的方式实现的线程隔离
# LocalStack封装了Local成为线程隔离的栈结构
# 封装可以解决问题，如果一次封装解决不了，那么就再来一次
# 编程也是一种艺术，适当的含蓄（封装）


# Locak对象对线程隔离的实现
# 此处处于主线程中
my_obj = Local()
my_obj.b = 1

def worker():
    my_obj.b = 2
    print('in new thread b is: ', my_obj.b)

new_t = threading.Thread(target=worker, name='vinson_thread')
new_t.start()

print('in main thread b is: ', my_obj.b)


