#!/usr/bin/env python
# Your factory should inherit from this class.

import sys

from .constants import *


class InvalidCommand(Exception):
    pass


class NoCommandGiven(Exception):
    pass


class BaseFactory:
    def __init__(self):

        self.loopCount = 0

        try:
            if sys.argv[1] == "run":
                self.run()
            else:
                raise InvalidCommand(
                    f"\n\nPlease use one of the following commands, not '{sys.argv[1]}': \n    - 'run'\n"
                )
        except (IndexError):
            raise NoCommandGiven(
                "\n\nPlease provide a command! Valid commands: \n    - 'run'\n"
            )

    @staticmethod
    def getInstance(self):
        return self

    def start(self):  # Overridden by programmer.
        pass

    def loop(self):  # Overriden by programmer.
        pass

    def dailyLoop(self):  # Overriden by programmer.
        pass

    def end(self):  # Overriden by programmer.
        pass

    def run(self):  # Basic loop procedure.
        try:
            self.start()
            self.dailyLoop()
            while True:
                if self.loopCount == (system.loopsPerDay - 1):
                    self.dailyLoop()
                    self.loopCount = 0
                else:
                    self.loop()
                    self.loopCount += 1

        except (KeyboardInterrupt):
            self.end()
