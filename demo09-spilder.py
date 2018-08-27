import urllib2

url="http://blog.csdn.net/happydeer"

req = urllib2.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
req.add_header('GET',url)
req.add_header('Referer','https://blog.csdn.net/happydeer')

html2 = urllib2.urlopen(req)
print(req.headers.items())
content = html2.read()
print(content)