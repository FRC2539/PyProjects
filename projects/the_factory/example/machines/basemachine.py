from random import randint

from resources.constants import *


class InvalidInput(Exception):
    pass


class BaseMachine:
    def __init__(
        self, nameOfMachine, basePurchaseCost=1, baseRepairCost=1, efficiencyLevel=1
    ):

        for inputs in [basePurchaseCost, baseRepairCost, efficiencyLevel]:
            if inputs <= 0:
                raise InvalidInput(f"No negative or zero inputs! ({inputs})")

        self.nameOfMachine = str(nameOfMachine)

        self.basePurchaseCost = basePurchaseCost
        self.baseRepairCost = baseRepairCost

        self.efficiencyLevel = efficiencyLevel  # 1 - 100. Add this with other machines to get the max efficiency.
        # Note: The more efficient a machine, the more it costs to manafacture and repair!
        self.chancesOfBreaking = self.efficiencyLevel / 4  # Between 1/4 and 25.

        self.employeesNeeded = int(self.efficiencyLevel / 5)  # More means worse!

        if self.employeesNeeded < 1:  # Ensures there is always someone.
            self.employeesNeeded = 1

        self.dailyProductCount = 0

    def setPurchaseCost(self, cost):
        self.basePurchaseCost = cost
        self.update()

    def setRepairCost(self, cost):
        self.baseRepairCost = cost
        self.update()

    def setEfficiency(self, level):
        self.efficiencyLevel = level
        self.update()

    def getPurchaseCost(self):
        return self.basePurchaseCost + (
            (self.efficiencyLevel / 100) * self.basePurchaseCost
        )

    def getRepairCost(self):
        return self.baseRepairCost + (
            (self.efficiencyLevel / 100) * self.baseRepairCost
        )

    def getEmployeeCount(self):
        return self.employeesNeeded

    def getMachineName(self):
        return self.nameOfMachine

    def updateChancesOfBreaking(self):
        self.chancesOfBreaking = self.efficiencyLevel / 4

    def updateEmployeesNeeded(self):
        self.employeesNeeded = int(self.efficiencyLevel / 10)

        if self.employeesNeeded < 1:
            self.employeesNeeded = 1

    def update(self):
        self.updateChancesOfBreaking()
        self.updateEmployeesNeeded()

    def didBreak(self):
        return randint(1, 100) < self.chancesOfBreaking

    def loop(self):  # Will be overriden.
        if self.didBreak():
            raise MachineBroke(self)
        else:
            self.dailyProductCount += self.efficiencyLevel

    def resetProduct(self):
        self.dailyProductCount = 0


class MachineBroke(Exception):
    def __init__(self, machineObj: BaseMachine):
        self.machine = machineObj
        self.repairCost = machineObj.getRepairCost()
        self.machineName = machineObj.getMachineName()
        super().__init__(f"Uh Oh! Looks like a {self.machineName} broke!")
