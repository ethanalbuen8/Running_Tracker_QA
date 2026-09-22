class DistanceCalculator:
    def __init__(self,pace,time):
        self.pace = pace
        self.time = time

    def distance_calculator(self):
        distance = (1 / self.pace) * self.time #Pace is inverse of speed, hence the (1 / self.pace).
        return round(distance,2)