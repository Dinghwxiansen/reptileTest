#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:dingxiansen
# datetime:2019/3/19 9:34
# software: PyCharm

import bs4

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs4.BeautifulSoup(open('demo.html'), 'lxml')

print(soup.prettify())

print(soup.head)
# <head><title>The Dormouse's story</title></head>
print(soup.title)
# <title>The Dormouse's story</title>

print(soup.body.b)
# <b>The Dormouse's story</b>

print(soup.body.p)
# <p class="title"><b>The Dormouse's story</b></p>

# 获取所有的标签
print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print(soup.find_all('a')[1])
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>


head = soup.head
print(head.contents)
# [<title>The Dormouse's story</title>]   这是一个列表

print(head.contents[0])
# <title>The Dormouse's story</title>    上面列表的第一个元素

print(head.contents[0].contents)
# ["The Dormouse's story"]

print('------------------')
# todo 通过tag.children生成器，可以对tag的子节点进行循环
for child in head.contents[0].children:
    print(child)
# The Dormouse's story

# TODO 遍历出子孙节点
for child in head.descendants:
    print(child)

# <title>The Dormouse's story</title>
# The Dormouse's story
print('---------------')


for string in soup.strings:
    print(string)
