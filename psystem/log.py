import logging
import logging.handlers
import os
import sys

__author__ = "Gokhan MANKARA"
__email__ = "gokhan@mankara.org"


class Log:
    def __init__(self, log_file_path=None):

        self.log_path = log_file_path

        if not log_file_path is None:

            path = os.path.dirname(self.log_path)

            if not os.path.exists(path):
                os.makedirs(path)
        
            self.logger = logging.getLogger('PSystem Logger')

            total_handlers = len(self.logger)

            if total_handlers == 0:
                self.logger.setLevel(logging.INFO)
                formatter = logging.Formatter('%(asctime)s %(levelname)-5s %(message)s', "%d %b %Y %H:%M:%S")

                handler = logging.handlers.TimedRotatingFileHandler(self.log_path, encoding='UTF-8',
                                                                    when='midnight', backupCount=5)
                handler.setFormatter(formatter)
                self.logger.addHandler(handler)

    def __output(self, level, message):

        if sys.stdout.isatty():
            print(message)

        elif self.log_path is None:
            print(message)

        else:

            if "debug" == level:
                self.logger.debug(message)
            elif "info" == level:
                self.logger.info(message)
            elif "error" == level:
                self.logger.error(message)
            elif "warn" == level:
                self.logger.warning(message)
            elif "crit" == level:
                self.logger.critical(message)
    
    def debug(self, message):
        self.__output("debug", message)

    def info(self, message):
        self.__output("info", message)
    
    def error(self, message):
        self.__output("error", message)

    def warning(self, message):
        self.__output("warn", message)

    def critical(self, message):
        self.__output("crit", message)


