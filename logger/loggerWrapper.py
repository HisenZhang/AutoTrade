import sys
import logging
import logging.handlers


class Logger(object):
    """
    Logger wrapper
    """

    def __init__(self, config, name='root'):

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            formatter = logging.Formatter(
                fmt=config.get('logging', 'LOG_FORMAT'),
                datefmt=config.get('logging', 'DATE_FORMAT'))

            # Write to file
            fileHandler = logging.handlers.TimedRotatingFileHandler(
                config.get('logging', 'LOG_FILE'),
                when='midnight',
                interval=1,
                backupCount=0)
            fileHandler.setLevel(logging.INFO)
            fileHandler.setFormatter(formatter)

            # Write to console
            stdoutHandler = logging.StreamHandler(sys.stdout)
            stdoutHandler.setLevel(logging.INFO)
            stdoutHandler.setFormatter(formatter)

            # TODO STMP alert

            self.logger.addHandler(fileHandler)
            self.logger.addHandler(stdoutHandler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
