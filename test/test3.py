# coding: utf-8
# 2019/7/6 13:22


__author__ = 'Vinson <me@vinsonwei.com>'

import threading
import time


# request = {key1: value1, key2:value2}
# 多线程唯一标识
# request = { thread_key1: Request1, ...}
# 用不同线程的id号


def worker():
    print('I am a thread')
    t = threading.current_thread()
    time.sleep(100)
    print(t.getName())

new_t = threading.Thread(target=worker, name='vinson_thread')

new_t.start()

t= threading.current_thread()
print(t.getName())


# 多线程可以充分利用CPU的性能优势

# Python不能充分利用多核CPU优势

# Python GIL（Global interpreter lock）