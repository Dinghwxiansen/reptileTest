#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:dingxiansen
# datetime:2019/3/14 17:27
# software: PyCharm

import requests

# r = requests.get("http://www.baidu.com")
#
# print(r.text)

# 发送请求
hd = {'user-agent': '123'}
r = requests.get('http://www.bilibili.com', headers=hd)
r2 = requests.post('http://www.baidu.com', data={'key': 'value'})

r3 = requests.get('https://api.github.com/events')
# print(r.request.headers)
# print(r2.text)
print(r3.request)
