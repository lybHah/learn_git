#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')
page='1'
url='http://www.qiushibaike.com/text/'
user_agent='Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent' : user_agent}
try:
	request=urllib2.Request(url,headers=headers)
	respone=urllib2.urlopen(request)
	content=respone.read().decode('utf-8')
	pattern=re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+'="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
	items=re.findall(pattern,content)
	for item in items:
		haveImg=re.search("img",item[3])
		if not haveImg:
			print item[0],item[1],item[2],item[3],item[4]
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason


