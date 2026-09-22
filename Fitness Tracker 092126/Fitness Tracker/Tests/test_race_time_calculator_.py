import pytest
from Model.race_time_calculator import RaceTimeCalculator

class TestRaceTimeCalculator:

    @pytest.mark.parametrize("dist,pace,expected_result", [

        (2,5,10),
        (1,4,4),
        (21,7.56,158.76)

    ])

    def test_race_time_calculator(self,dist,pace,expected_result): #Why does it not need self?
        trtc = RaceTimeCalculator(dist,pace)
        assert trtc.race_time() == expected_result
