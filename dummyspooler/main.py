import tornado.ioloop
import tornado.web



class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        super(MainHandler, self).initialize()

    def post(self):
        self.write({'success': 1, 'message': 'Great Success'})

if __name__ == '__main__':
    app = tornado.web.Application([(r'^/', MainHandler)])
    app.listen(1234)
    tornado.ioloop.IOLoop.current().start()
