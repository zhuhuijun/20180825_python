import tornado.web
import tornado.ioloop
import os
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello,world\n")
    def post(self):
        self.write("hello,world>>>post\n")
    def put(self):
        self.write("hello,world>>>put\n")
        pass
    def delete(self):
        self.write("hello,world>>>delete\n")
        
if __name__ =="__main__":
    settings={
    'debug':True,
    'static_path':os.path.join(os.path.dirname(__file__),'static'),
    'template_path':os.path.join(os.path.dirname(__file__),'tmp')
    }

    application = tornado.web.Application([
        (r"/",MainHandler),
        ],**settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()