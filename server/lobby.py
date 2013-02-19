#!/usr/bin/python

Lobbies = []
Lobby = []

def join(sock):
    LobbySet = set(Lobby)
    LobbySet.append(sock)
    Lobby = list(LobbySet)

def leave(sock):
    if sock in Lobby:
        Lobby.remove(sock)
    else:
        pass
