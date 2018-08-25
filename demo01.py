# _*_ coding:utf-8 _*_
import urllib

url='http://www.iplaypython.com'
html = urllib.urlopen(url)
content = html.read()
#print(html.read())
print(html.getcode())
print(html.geturl())
print(html.info())