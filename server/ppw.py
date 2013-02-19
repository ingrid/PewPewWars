#!/usr/bin/python

import tornado.web
from tornado import websocket

import lobby

# Test function.
class LobbyWebSocket(websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"
        return lobby.join(self)

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"

class GameWebSocket(websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"

class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"
        lobby.leave(self)

class ClientHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
