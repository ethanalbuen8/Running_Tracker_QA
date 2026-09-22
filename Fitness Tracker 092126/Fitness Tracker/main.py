from Model.distance_calculator import DistanceCalculator
from Model.pace_calculator import PaceCalculator
from Model.race_time_calculator import RaceTimeCalculator

class Main:

    while True: 

        try:
            print("========================================================================\n")
            print("1: Distance Calculator")
            print("2: Pace Calculator")
            print("3: Race Time Calculator\n")
            option = int(input("Welcome to Running Tracker! Choose the options above typing the number: "))
            print("========================================================================\n")

            match option:

                case 1:

                    print("You chose Distance Calculator.")
                    km_or_mi = input("Choose km or mi: ")
                    print(f"You chose {km_or_mi}.")

                    pace = float(input(f"Type your pace in min/{km_or_mi}: "))
                    time = float(input("Type duration you ran in mins: "))

                    dc = DistanceCalculator(pace,time)
                    dist = dc.distance_calculator()

                    print("\n========================================================================")
                    print(f"You ran {dist} {km_or_mi}")
                    print("========================================================================\n")
                    break

                case 2:

                    print("You chose Pace Calculator.")
                    km_or_mi = input("Choose km or mi: ")
                    print(f"You chose {km_or_mi}.")

                    time = float(input("Type duration you ran in mins: "))
                    dist = float(input(f"Type distance you ran in {km_or_mi}: "))

                    pc = PaceCalculator(time,dist)
                    pace = pc.pace_calculator()

                    print("\n========================================================================")
                    print(f"You ran at {pace} mins/{km_or_mi}.")
                    print("========================================================================\n")
                    break

                case 3:

                    print("You chose Race Time Calculator.")
                    km_or_mi = input("Choose km or mi: ")
                    print(f"You chose {km_or_mi}.")
                                        
                    dist = float(input(f"Type distance you ran in {km_or_mi}: "))
                    pace = float(input(f"Type your pace in min/{km_or_mi}: "))
                                        
                    rtc = RaceTimeCalculator(dist,pace)
                    time = rtc.race_time()
                    print("\n========================================================================")
                    if time >= 60:
                        hr = time / 60
                        print(f"Hr: {int(hr)}")
                        if hr % 2 != 0:
                            hr_dec = hr - int(hr) #No extra zeros
                            min = round(hr_dec * 60)
                            print(f"Min: {min}")
                            print(f"You ran {int(hr)} hr {min} min")
                        if min % 2 != 0:
                            min_dec = min - int(min) #No extra zeros, carry the decimal
                            sec = round(min_dec * 60)
                            print(f"Sec: {sec}")
                            print(f"You ran {int(hr)} hr {min} min {sec} sec")
                    else:
                        print(f"You ran {time} mins")
                    print("========================================================================\n")
                    break

                case _:
                    print("Invalid input\n")

        except:
            print("========================================================================\n")
            raise ValueError("Invalid input type. Please only enter integers 1 to 3.")