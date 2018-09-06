#coding:utf-8
import tornado.ioloop
import tornado.web
import os


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
        self.write(result)
class LoginHandler(BassHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name:<input type="text" name="name">'
                   '<input type="submit" value="sign in">'
                   '</form></body></html>')
    def post(self):
        self.set_secure_cookie("user",self.get_argument('name'))
        self.redirect('/')


settings={
    'cookie_secret':'lll/vo=',
    'login_url':'/login',
    'template_path':os.path.join(os.path.dirname(__file__),'template'),
    'debug':True
}
application = tornado.web.Application([
    (r'/',MainHandler),
    (r'/login',LoginHandler),
    (r'/weibo/add',WeiboHandler),
    ],**settings)
if __name__ == "__main__":
    application.listen(8888)
    print('8888:listening...')
    tornado.ioloop.IOLoop.instance().start()
    print('8888:listening...')

