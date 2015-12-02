import tornado.ioloop
import tornado.web
import markup

jobs = []


class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        super(MainHandler, self).initialize()

    def post(self):
        global jobs
        jobs.append({k: self.get_argument(k) for k in self.request.arguments})
        self.write({'success': 1, 'message': 'Great Success'})

    def get(self):
        global jobs
        page = markup.page()
        page.init(title='Spooler Jobs')
        page.h1('Requested jobs')
        page.ul()
        for job in jobs:
            page.li(' '.join(['%s:%s'%(k, v) for k, v in job.iteritems()]))
        page.ul.close()
        self.write(str(page))


if __name__ == '__main__':
    app = tornado.web.Application([(r'^/.*', MainHandler)])
    app.listen(1234)
    tornado.ioloop.IOLoop.current().start()
