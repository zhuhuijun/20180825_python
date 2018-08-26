#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import urllib
import os

def callback(a,b,c):
    ###
    #@a:
    #@b:
    #@c:
    ###
    downprocess = 100.0*a*b/c
    if downprocess>100:
        downprocess = 100
    print('downprocess:%.2f%%'%(downprocess))
url='http://www.iplaypython.com'
url2= 'http://www.tudou.com'
mypath = os.path.join(os.path.dirname(__file__),'static/aa.html')
print(mypath)
urllib.urlretrieve(url,mypath,callback)
info = urllib.urlopen(url2).info()
print(info)
print(info.getparam('charset'))
###

###