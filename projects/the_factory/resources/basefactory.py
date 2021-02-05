#!/usr/bin/env python
# Your factory should inherit from this class. 

import sys, shutil

class BaseFactory:
    
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance(self):
        return self
    
    def start(self): # Overridden by programmer. 
        pass
    
    def loop(self): # Overriden by programmer.
        pass
    
    def begin(self): # Basic loop procedure. 
        self.start()
        while True:
            self.loop()

def run():
    if __name__ == '__main__':
        if sys.argv[1] == "run":
            pass
        
