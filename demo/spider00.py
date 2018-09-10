# _*_ coding:utf-8 _*_
import urllib
import re

r = re.compile(r'href="(https://blogs\.csdn\.net.+?)"')

def geturlsFromurl(url):
    try:
        opener = urllib.urlopen(url)
        contents = opener.read()
        print(contents)
        g = r.fintiter(contents)
        opener.close()
        print(g)
        return g
    except Exception as e:
        print('s'+e.message)
        return[]

def getUrl(url,datacache,i):
    urls = geturlsFromurl(url)
    print(len(urls))
    for m in urls:
        mm = m.groups()[0]
        if mm not in datacache:
            datacache.append(mm)
        else:
            continue
        i = i+1
        print(i)
        print(len(datacache))
        getUrl(mm,datacache,i)
data_cache=[]
i=0
getUrl('https://blogs.csdn.net/',data_cache,i)