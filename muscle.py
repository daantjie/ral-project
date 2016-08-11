
class Muscle (Organ):

    def __init__(self, innards):
        super().__init__(innards)

    def turn(self, angle, power=5):
        self.innards.turn(power, angle)
