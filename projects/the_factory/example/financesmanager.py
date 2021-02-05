from machines.basemachine import BaseMachine


class Profit:  # Reuse these.
    def __init__(self, startingBalance=0):
        self.balance = startingBalance
        self.transactions = 0

    def add(self, val):
        self.balance += val
        self.transactions += 1

    def getBalance(self):
        return self.balance

    def getTransactionCount(self):
        return self.transactions


class FinanceManager:  # Create one of these.
    def __init__(self, machines: [BaseMachine], startingBalance=0):
        self.balance = startingBalance
        self.transactionsPerLoop = (
            []
        )  # Each index holds the number of transactions that loop.
        self.machineFailures = {}

        self.currentProfitObj = Profit()

    def getBalance(self):
        return self.balance

    def getTotalTransactions(self):
        tt = 0
        for transaction in self.transactionsPerLoop:
            tt += transaction

        return tt

    def getMachineFailures(self):
        return self.machineFailures

    def repairMachine(self, machineThatBroke: BaseMachine):
        self.balance -= machineThatBroke.getRepairCost()

        name = machineThatBroke.getMachineName()

        if name in list(self.machineFailures.keys()):
            original = self.machineFailures[name]
            self.machineFailures[name] = original + 1

        else:
            self.machineFailures[name] = 1

    def merge(self, profit: Profit):
        self.balance += profit.getBalance()
        self.transactionsPerLoop.append(profit.getTransactionCount())

    def inDebt(self):
        return self.balance <= 0

    def printAll(self):
        print("Balance: $" + str(self.balance))
        print("Machine Failures: " + str(self.machineFailures))
        print("Transactions: " + str(len(self.transactionsPerLoop)))

    def loop(self, moola):
        self.currentProfitObj.add(moola)

    def dailyLoop(self, electric, employees):
        self.currentProfitObj.add(-1 * electric)  # Add the day's electric.
        self.currentProfitObj.add(-1 * employees)

        self.merge(self.currentProfitObj)  # Add this day's profit to the total.

        del self.currentProfitObj  # Erase it entirely.
        self.currentProfitObj = Profit()
