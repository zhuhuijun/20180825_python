# _*_ codeing:utf-8 _*_
import urllib
url="http://www.163.com/"
html = urllib.urlopen(url)
#content =html.read().decode('gbk','ignore').encode('utf-8')
#print(content)
code = html.getcode()
if  code==200:
    print('ok')
    print(html.info())
else:
    print('error')