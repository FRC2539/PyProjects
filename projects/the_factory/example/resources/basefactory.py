#!/usr/bin/env python
# Your factory should inherit from this class. 

import sys

class InvalidCommand(Exception):
    pass

class BaseFactory:
    
    def __init__(self):
        if sys.argv[1] == 'run':
            self.run()
        else:
            raise InvalidCommand(f'\n\nPlease use one of the following commands, not \'{sys.argv[1]}\': \n    - \'run\'\n')
    
    @staticmethod
    def getInstance(self):
        return self
    
    def start(self): # Overridden by programmer. 
        pass
    
    def loop(self): # Overriden by programmer.
        pass
    
    def end(self): # Overriden by programmer.
        pass
    
    def run(self): # Basic loop procedure. 
        try:
            self.start()
            while True:
                self.loop()
        except(KeyboardInterrupt):
            self.end()