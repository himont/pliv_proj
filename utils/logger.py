import logging
import logging.handlers
from os.path import join, isdir, dirname
from os import makedirs, chmod, umask
from settings.config import *

class logger_class():
    @staticmethod
    def create_logger():


        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # create a file handler
        handler = logging.handlers.TimedRotatingFileHandler(
                                                            LOG_DIR+'automation.log',
                                                            when='H', interval=1,
                                                            backupCount=24,
                                                            encoding=None,
                                                            delay=False,
                                                            utc=False)
        handler.setLevel(logging.INFO)

        # create a logging format
        formatter = logging.Formatter(
                                      '%(asctime)s - [%(filename)s:%(lineno)s - %(funcName)20s() ] - '
                                  '%(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(handler)
        return logger
