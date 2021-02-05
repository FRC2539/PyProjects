from machines.basemachine import BaseMachine


class PropertyManager:
    def __init__(
        self, machines: [BaseMachine], maxNumOfMachines=1, electricCostPerMachine=100
    ):
        self.maxNumOfMachines = maxNumOfMachines
        self.machines = machines

        self.totalEmployeeCount = 0

        for machine in self.machines:
            self.totalEmployeeCount += machine.getEmployeeCount()

        self.totalElectricCost = electricCostPerMachine * len(self.machines)

        self.totalProducts = 0

    def getElectricCost(self):
        return self.totalElectricCost

    def getTotalEmployees(self):
        return self.totalEmployeeCount

    def getTotalProducts(self):
        return self.totalProducts

    def getMachines(self):
        return self.machines

    def printAll(self):
        print("Machine Count: " + str(len(self.machines)))
        print("Max Num. of Machines: " + str(self.maxNumOfMachines))
        print("Electric Bill: $" + str(self.totalElectricCost))
        print("Total Employees: " + str(self.totalEmployeeCount))

    def loop(self):
        for machine in self.machines:
            machine.loop()
            self.totalProducts += machine.dailyProductCount

    def dailyLoop(self):
        self.totalProducts = 0
        for machine in self.machines:
            machine.resetProduct()
