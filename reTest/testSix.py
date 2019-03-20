#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:dingxiansen
# datetime:2019/3/18 10:11
# software: PyCharm

# todo 响应内容
import requests


r = requests.get('https://api.github.com/events')
# print(r.text)

print(r.content)

# [{"id":"9259823759","type":"PushEvent","actor":
# {"id":32785837,"login":"brucejh99","display_login":"brucejh99","gravatar_id":"",
# print(r.encoding)
#  utf-8

