# coding: utf-8
# 2019/6/27 21:02

__author__ = 'Vinson <me@vinsonwei.com>'


import requests


class HTTP:
    @classmethod
    def get(cls, url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text


