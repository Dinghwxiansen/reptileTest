#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:dingxiansen
# datetime:2019/3/18 9:43
# software: PyCharm

# todo 传递URL参数
import requests

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

r = requests.get("http://httpbin.org/get", params=payload)

print(r.url)
# http://httpbin.org/get?key1=value1&key2=value2
