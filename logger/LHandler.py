import logging
from logger import LHandler

"""
def debug(dlogmsg):
    logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s -> %(message)s')
    logging.debug(dlogmsg)
"""
def critical(clogmsg):
    logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s -> %(message)s')
    logging.critical(clogmsg)

def error(elogmsg):
    logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s -> %(message)s')
    logging.error(elogmsg)

def warning(wlogmsg):
    logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s -> %(message)s')
    logging.warning(wlogmsg)
"""
def info(ilogmsg):
    logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s -> %(message)s')
    logging.info(ilogmsg)
"""  

def LogInit():
    lstrt = 1
    for _ in range(lstrt):
        LHandler.warning("This log file resets after every run.")