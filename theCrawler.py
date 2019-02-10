#!python3
# -*- coding:utf-8 -*-
import urllib, re, sys, requests

weiboHotFile = requests.get('https://s.weibo.com/top/summary')
weiboHotHtml = weiboHotFile.text.replace('\n', '').replace('\t', '').replace(' ', '')

# 正则
hotKey = re.compile(r'tdclass="td-02"><ahref="/weibo\?(.*?)&Refer=top')
msg = hotKey.findall(weiboHotHtml)
for i in msg:
    print(i)
