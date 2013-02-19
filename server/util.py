#!/usr/bin/python
import logging
import jsonlogger

def getLogger(name=""):
    logger = logging.getLogger(name)
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

    return logger

def unpack(data):
    pass

def pack(data):
    pass
