#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:dingxiansen
# datetime:2019/3/15 16:02
# software: PyCharm


from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>"""

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

# 文档的title
print(soup.title)
# <title>The Dormouse's story</title>

# title的name值
print(soup.title.name)
# title

# title中的字符串string
print(soup.title.string)
#  The Dormouse's story

# title的父亲节点的name属性
print(soup.title.parent.name)
# head

# 文档的第一个找到的段落
print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

# 找到的p的class属性值
print(soup.p['class'])
# ['title']

# 找到a标签
print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print('--------')

# 找到所有的a标签
print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print('--------')

# 找到ID值等于3的‘a’标签
print(soup.find(id="link3"))
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# 从文档中找到所有的<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))

# 从文档中获取所有文字的内容
print(soup.get_text())


