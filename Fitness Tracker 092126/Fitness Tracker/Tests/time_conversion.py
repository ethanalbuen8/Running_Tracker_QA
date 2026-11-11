class TimeConversion:
    def __init__(self,time):
        self.time = time

    def convert(self):
        seconds = self.time * 60

        hr = seconds / 3600
        
        remainder = hr - int(hr)
        
        mins = remainder * 60
        
        remainder = mins - int(mins)
        
        sseconds = remainder * 60
        print(sseconds)

        #Nested if/else statements to determine the appropriate time format
        if hr < 1:
            if mins < 1:
                return f'{round(sseconds)} seconds'
            elif sseconds < 1:
                return f'{int(mins)} mins'
            else:
                return f'{int(mins)} mins {round(sseconds)} seconds'

        else:
            if mins < 1 and sseconds < 1:
                return f'{int(hr)} hrs'    
            elif sseconds > 59:
                return f'{int(hr)} hrs {round(mins)} mins'
            else:
                return f'{int(hr)} hrs {int(mins)} mins {round(sseconds)} seconds'
