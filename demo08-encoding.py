# _*_ coding:utf-8 _*_
import urllib

url="http://blog.csdn.net/yuanmeng001"

html = urllib.urlopen(url)
content = html.read()
print(content)