#!/usr/bin/env python3

"""
This class is the head class. The management system. 
The overall grand daddy. From here, we have the building management
(including all the machines), the finance manager, and 
the employment directory. 
"""

from resources.constants import *

from resources.basefactory import *  # Import the parent class.

from machines.basemachine import MachineBroke
from machines.dispensemachine import DispenseMachine

from financesmanager import FinanceManager
from propertymanager import PropertyManager


class CocaColaFactory(BaseFactory):
    def start(self):  # Add things you want to run once here.
        self.fm = FinanceManager(self.machines, startingBalance=0)  # Start with $0
        self.pm = PropertyManager(
            self.machines, 10, electricCostPerMachine=300
        )  # $300 electric for machine per loop.

    def loop(
        self,
    ):  # Add things you want to loop here. Runs individually, many times. This makes the product.
        try:
            self.pm.loop()
        except MachineBroke as errorObj:
            self.fm.repairMachine(errorObj.machine)

        moola = self.pm.getTotalProducts() * product.sellPrice

        self.fm.loop(moola)

    def dailyLoop(self):  # Runs every 'day'
        self.fm.dailyLoop(
            self.pm.getElectricCost(),
            (
                self.pm.getTotalEmployees()
                * system.employeeHourlyWage
                * system.workdayLength
            ),
            self.pm.getTotalProducts() * system.exportCost,
        )  # Pays electric and employees every day. Also ships out products every day.
        self.pm.dailyLoop()

    def end(self):  # Add things you want to do upon ending here.
        print("\n")
        self.fm.printAll()
        self.pm.printAll()

    def __init__(self):

        self.machines = [DispenseMachine(), DispenseMachine()]

        super().__init__()


CocaColaFactory()  # Create the object to begin this whole thing.
