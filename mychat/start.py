# _*_ coding:utf-8 _*_
import os
import tornado.ioloop
import tornado.web
import tornado.websocket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    connects = set()
    def open(self):
        print "socket opened"
        ChatSocketHandler.connects.add(self)

    def on_message(self, message):
        ChatSocketHandler.send_all(message)

    def on_close(self):
        print "socketed closed"    

    @classmethod
    def send_all(cls, chat):
        for connect in cls.connects:
            try:
                connect.write_message(chat)
            except:
                pass

if __name__ =="__main__":
    settings={
    "debug":True,
    "template_path": os.path.join(os.path.dirname(__file__), "templates")
    }
    app = tornado.web.Application([
        (r"/",MainHandler),
        (r"/websocket",ChatSocketHandler),
        ],**settings)
    app.listen(8181)
    tornado.ioloop.IOLoop.instance().start()
    print('8181 had listening')