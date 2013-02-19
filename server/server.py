#!/usr/bin/python

import tornado.ioloop

from urls import url_list

if __name__ == "__main__":
    application = tornado.web.Application(url_list)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
