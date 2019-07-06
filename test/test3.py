# coding: utf-8
# 2019/7/6 13:22

__author__ = 'Vinson <me@vinsonwei.com>'

import threading

def worker():
    print('I am a thread')
    t = threading.current_thread()
    print(t.getName())

new_t = threading.Thread(target=worker, name='vinson_thread')

new_t.start()

t= threading.current_thread()
print(t.getName())

