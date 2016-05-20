import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import tornado.httpserver


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, World")


class WebHookHandler(RequestHandler):
    def get(self):
        print self.get_query_arguments('hub_verify_token')


def make_app():
    return tornado.web.Application([(r"/webhook",WebHookHandler)
        ,(r"/*",MainHandler)])


if __name__ == '__main__':
    app = make_app()

    '''
    http_server = tornado.httpserver.HTTPServer(app, ssl_options={
        "certfile": "/etc/ssl/certs/apache-selfsigned.crt",
        "keyfile": "/etc/ssl/private/apache-selfsigned.key"
    })
    http_server.listen(443)
    '''

    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()
