#_*_ coding:utf-8 _*_
import re
import urllib
from bs4 import BeautifulSoup
def get_content(url):
    """ doc. """
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    
    return content

def getImages(info):
    """ .doc"""
    soup = BeautifulSoup(info,features="html.parser")
    allimg = soup.find_all('img',class_='BDE_Image')
    i=0
    for one in allimg:
        print(one['src'])
        urllib.urlretrieve(one['src'],'%s.jpg'%(str(i)))
        i +=1
if __name__ == '__main__':
    myurl='http://tieba.baidu.com/p/2772656630'
    info = get_content(myurl)
    getImages(info)