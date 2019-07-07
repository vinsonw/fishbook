# coding: utf-8
# 2019/7/8 0:55
import threading
import time

__author__ = 'Vinson <me@vinsonwei.com>'

from werkzeug.local import  LocalStack


my_stack = LocalStack()
my_stack.push(1)

print('in main thread after first push, value is: ', my_stack.top)

def worker():
    # 新线程
    print('in new thread before push, value is:', my_stack.top)
    my_stack.push(2)
    print('in new thread after push, value is:', my_stack.top)

new_t = threading.Thread(target=worker, name='vinson_thread')
new_t.start()
time.sleep(1)

# 主线程
print('finally, in main thread value is:', my_stack.top)
