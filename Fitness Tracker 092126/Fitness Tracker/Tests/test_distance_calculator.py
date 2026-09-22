import pytest
from Model.distance_calculator import DistanceCalculator

class TestDistanceCalculator:
    @pytest.mark.parametrize("pace,time,expected_result", [

        (4,20,5),
        (6,42,7),
        (5,55,11)

    ])

    def test_distance_calculator(self,pace,time,expected_result):
        #Create an object
        tdc = DistanceCalculator(pace,time)
        assert tdc.distance_calculator() == expected_result

# Same behavior being tested + different data → consider parameterization.