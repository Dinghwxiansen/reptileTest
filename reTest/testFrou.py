#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:dingxiansen
# datetime:2019/3/15 9:35
# software: PyCharm

import requests

from reTest.testThree import getHtmlText

r = getHtmlText("http://www.baidu.com")

print(r)
