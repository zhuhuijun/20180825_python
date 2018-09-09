#coding:utf-8
import tornado.ioloop
import tornado.web
import os
import re
from mongo import db


def getLabs(str):
    r = re.compile(ur'@([\u4E00~\u9FA5\w~]+)')
    return r.findall(str)


class BassHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BassHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("hello:"+name)

class WeiboHandler(BassHandler):
    @tornado.web.authenticated
    def get(self):
        return self.render('weibo_add.html')
    def post(self):
        result = self.get_argument("content",None)
        con = getLabs(result)
        print(con)
        db.logs.insert({'content':result,'user':self.get_current_user()})
        self.write(result)
class LoginHandler(BassHandler):
    def get(self):
        self.render('login.html')
    def post(self):
        self.set_secure_cookie("user",self.get_argument('name'))
        self.redirect('/')

class RegisterHandler(BassHandler):
    def get(self):
        return self.render('user_add.html')
    def post(self):
        username = self.get_argument('username')
        userpwd = self.get_argument('userpwd')
        if username == '' or userpwd == '':
            self.write('username or pwd is empty')
        if db.users.count({"username":username})>0:
            self.write('this count had registered')
        self.set_secure_cookie("user",username)
        db.users.insert({"username":username,"userpwd":userpwd})
        self.redirect('/userinfo')
class UserinfoHandler(BassHandler):
    @tornado.web.authenticated
    def get(self):
        user = self.get_current_user()
        return self.render('userinfo.html',**{"user":user})
            
settings={
    'cookie_secret':'lll/vo=',
    'login_url':'/login',
    'template_path':os.path.join(os.path.dirname(__file__),'template'),
    'debug':True
}
application = tornado.web.Application([
    (r'/',MainHandler),
    (r'/login',LoginHandler),
    (r'/register',RegisterHandler),
    (r'/userinfo',UserinfoHandler),
    (r'/weibo/add',WeiboHandler),
    ],**settings)
if __name__ == "__main__":
    application.listen(8888)
    print('8888:listening...')
    tornado.ioloop.IOLoop.instance().start()
    print('8888:listening...')

