import logging
import logging.handlers
from os.path import join, isdir, dirname
from os import makedirs, chmod, umask
from settings.config import *

class logger_class():
    @staticmethod
    def create_logger():
        logger = logging.getLogger()
        log_values = { 'CRITICAL': 50,
                                'ERROR': 40,
                                'WARNING': 30,
                                'INFO': 20,
                                'DEBUG': 10,
                                'NOTSET': 0,
                                }
        logger.setLevel(log_values[LOG_LEVEL])

        # create a file handler
        handler = logging.handlers.TimedRotatingFileHandler(
                                                            LOG_DIR+'automation.log',
                                                            when='D', interval=1,
                                                            backupCount=30,
                                                            encoding=None,
                                                            delay=False,
                                                            utc=False)
        # create a logging format
        formatter = logging.Formatter(
                                      '%(asctime)s - [%(filename)s:%(lineno)s - %(funcName)20s() ] - '
                                  '%(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(handler)
        return logger
