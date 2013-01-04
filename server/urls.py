from tornado.web import url

from ppw import echo

url_list = [
    (r"/ws/echo", echo)
]
