import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import tornado.httpserver


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, World")


def make_app():
    return tornado.web.Application([(r"/*",MainHandler)])


if __name__ == '__main__':
    app = make_app()

    '''
        http_server = tornado.httpserver.HTTPServer(app, ssl_options={
            "certfile": "/root/ia.csr",
            "keyfile": "/root/ia.key",
        })
        http_server.listen(443)
    '''

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
