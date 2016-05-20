import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, World")


def make_app():
    return tornado.web.Application([(r"/*",MainHandler)])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
