# Project imports
from extras import utils 

# Third party imports
import sys
from asterisk import manager


class Ami:
    def __init__(self):
        self.manager = manager.Manager()
        self.config = utils.SecureConfig().asterisk

    def connect():
        self.manager.connect(self.config['host'])
        self.manager.login(self.config['user'], self.config['password'])
