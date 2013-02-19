#!/usr/bin/python
from tornado.web import url

from ppw import LobbyWebSocket, GameWebSocket, EchoWebSocket

url_list = [
    (r"/ws/lobby", LobbyWebSocket),
    (r"/ws/game", GameWebSocket),
    (r"/ws/echo", EchoWebSocket),
]
