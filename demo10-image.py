#_*_ coding:utf-8 _*_
import re
import urllib
def get_content(url):
    """ doc. """
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    
    return content

if __name__ == '__main__':
    myurl='http://tieba.baidu.com/p/2772656630'
    print(get_content(myurl))
