##!/usr/bin/env python
#day7 Request & BeautifulSoup

from email import header
from http import cookies
from urllib import request
from webbrowser import Chrome
import requests as req
from cgitb import html
from bs4 import BeautifulSoup

url = 'https://twitter.com/home?lang=zh-tw'
r = req.get(url)
print(r)
#if r.status_code == req.codes.ok:
#    print(r.text)

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 64.0.3282.186 Safari/537.36'
}
q = req.get('https://irs.thsrc.com.tw/IMINT/', headers = headers)
print(q)

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
cookies = {'over18':'1'}
p = req.get(url, cookies = cookies)
print(p)

url = 'http://ehappy.tw/bsdemo1.htm'
html = req.get(url)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'html.parser')
print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.p)