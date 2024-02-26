import logging

from patterns.creational_patterns.singleton import Singleton


class CustomLogger(metaclass=Singleton):

    def __init__(self):
        self.logger = logging.getLogger('main_logger')
        self.logger.setLevel(logging.DEBUG)

        self.file_handler = logging.FileHandler('logs/game.log')

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)
