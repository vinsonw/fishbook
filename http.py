# coding: utf-8
# 2019/6/27 21:02

__author__ = 'Vinson <me@vinsonwei.com>'


import requests


class HTTP:
    def get(self, url, return_json=True):
        r = requests.get(url)
        if return_json:
            return r.json()
        else:
            return r.text


