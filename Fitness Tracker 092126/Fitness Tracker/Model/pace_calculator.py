class PaceCalculator:
    def __init__(self,time,distance):
        self.time = time
        self.distance = distance

    def pace_calculator(self):
        pace = self.time / self.distance
        return round(pace,2)