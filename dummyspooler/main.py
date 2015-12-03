import tornado.ioloop
import tornado.web
import markup

jobs = []


class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        super(MainHandler, self).initialize()

    def post(self):
        global jobs
        jobs.append(self.request.arguments['job_name'])
        self.write({'success': 1, 'message': 'Great Success'})


class JobsHandlers(tornado.web.RequestHandler):
    def get(self):
        global jobs
        page = markup.page()
        page.init(title='Spooler Jobs')
        page.h1('Requested jobs')
        page.ul()
        for job in jobs:
            page.li(job)
        page.ul.close()
        self.write(str(page))

if __name__ == '__main__':
    app = tornado.web.Application([(r'^/jobs$', JobsHandlers),
                                   (r'^/.*', MainHandler)])
    app.listen(1234)
    tornado.ioloop.IOLoop.current().start()
