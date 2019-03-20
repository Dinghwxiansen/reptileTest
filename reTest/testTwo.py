#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:dingxiansen
# datetime:2019/3/14 17:34
# software: PyCharm

import requests

r = requests.get("http://www.bilibili.com")

# HTTP请求的返回状态，200表示成功，404表示失败
print(r.status_code)
# HTTP请求中的headers
print(r.headers)
# 从header中猜测的响应的内容编码方式
print(r.encoding)
# 从内容中分析的编码方式
print(r.apparent_encoding)
# 响应内容的二进制形式
print(r.content)

print(r)


