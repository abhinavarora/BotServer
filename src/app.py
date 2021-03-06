import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import tornado.httpserver
import os

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, World")


class WebHookHandler(RequestHandler):
    def get(self):

        print "Chor" + str(self.get_query_argument('hub.verify_token'))
        if self.get_query_argument('hub.verify_token') == 'TERA_BAAP_KAUN_HAI_BC':
            self.write(self.get_query_argument('hub.challenge'))
        else:
            self.write("")


def make_app():
    return tornado.web.Application([(r"/webhook",WebHookHandler)
        ,(r'/(favicon.ico)', tornado.web.StaticFileHandler, {"path": ""}),(r"/*",MainHandler)])


if __name__ == '__main__':
    app = make_app()

    '''
    http_server = tornado.httpserver.HTTPServer(app, ssl_options={
        "certfile": "/etc/ssl/certs/apache-selfsigned.crt",
        "keyfile": "/etc/ssl/private/apache-selfsigned.key"
    })
    http_server.listen(443)
    '''

    #app.listen(8888)

    http_server = tornado.httpserver.HTTPServer(app)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)

    tornado.ioloop.IOLoop.current().start()
