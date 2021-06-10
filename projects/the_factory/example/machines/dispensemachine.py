from .basemachine import BaseMachine


class DispenseMachine(BaseMachine):
    def __init__(self, nameOverride="Dispensing Machine"):
        super().__init__(
            nameOverride,  # Name of machine.
            basePurchaseCost=14000,  # BASE cost of purchase. Will be modified by efficiency level.
            baseRepairCost=2000,
            efficiencyLevel=10,
        )

    def rotateClockwise(self):
        pass

    def stopRotating(self):
        pass

    def rotateCounterClockwise(self):
        pass

    def dispenseSoda(self):
        pass

    def loop(self):  # This command will loop.
        super().loop()  # This calls neccessary, standard machine procedures (like didBreak()).

        self.rotateClockwise()  # Custom to each machine.
        self.stopRotating()
        self.dispenseSoda()
