#_*_ coding:utf-8 _*_
import re
import urllib
def get_content(url):
    """ doc. """
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    
    return content

def getImages(info):
    """ .doc"""
    regx=r'class="BDE_Image" src="(.+?\.jpg)"'
    pat = re.compile(regx)
    images_code = re.findall(pat,info)
    print(images_code)
    print("image len:%d"%(len(images_code)))

    i=0
    for imgurl in images_code:
        print(imgurl)
        urllib.urlretrieve(imgurl,'%s.jpg'%(str(i)))
        i +=1
if __name__ == '__main__':
    myurl='http://tieba.baidu.com/p/2772656630'
    info = get_content(myurl)
    getImages(info)