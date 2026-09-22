import pytest
from Model.pace_calculator import PaceCalculator

class TestPaceCalculator: #Lesson: Even classes have to start with Test
    
    @pytest.mark.parametrize("time, dist, expected_result", [
        (40,5,8),
        (80,10,8),
        (70,14,5)
    ])
    
    def test_pace_calculator(self,time,dist,expected_result):
        tpc = PaceCalculator(time,dist)
        assert tpc.pace_calculator() == expected_result