class RaceTimeCalculator:
    def __init__(self,distance,pace):
        self.distance = distance
        self.pace = pace

    def race_time(self):
        time = self.distance * self.pace
        return round(time,2)