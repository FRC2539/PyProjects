#!/usr/bin/env python3

"""
This class is the head class. The management system. 
The overall grand daddy. From here, we have the building management
(including all the machines), the finance manager, and 
the employment directory. 
"""

from resources.basefactory import * # Import the parent class.

class CocaColaFactory(BaseFactory):

    def start(self): # Add things you want to run once here. 
        print('start')
        
    def loop(self): # Add things you want to loop here.
        print('looping')
        
    def end(self): # Add things you want to do upon ending here.
        print('end')

    def __init__(self):
        super().__init__()
        
CocaColaFactory() # Create the object to begin this whole thing.