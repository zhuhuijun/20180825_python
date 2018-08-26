#!/usr/bin/env python
import urllib
import chardet #charset check#

def automatic_detect(url):
    content = urllib.urlopen(url).read()
    result = chardet.detect(content)
    encoding = result['encoding']
    return encoding
url='http://www.iplaypython.com'
content = urllib.urlopen(url).read()
print(chardet.detect(content))

print(automatic_detect(url))

urls=[
    'http://www.baidu.com',
    'http://www.sina.com'
]
for t in urls:
    print("%s:%s"%(t,automatic_detect(t)))
