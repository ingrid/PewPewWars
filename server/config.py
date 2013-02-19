#!/usr/bin/python
import logging
import jsonlogger

def setup_logger(name=__name__):
    logger = logging.getLogger(name)

    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
