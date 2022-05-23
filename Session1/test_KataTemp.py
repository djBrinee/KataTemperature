import pytest

from KataTemp import Temperature
from KataTemp import TemperatureScale

a = Temperature(20, TemperatureScale[2])

# Scenario 1, add
@pytest.mark.parametrize(
    "temp, expected",
    [
        (Temperature(10, TemperatureScale[1]), "303.15ºK"),
        (Temperature(50, TemperatureScale[0]), "303.15ºK")
    ]
)
def test_add(temp, expected):
    assert a.add(temp).ToString() == expected

# Scenario 2, substract
b = Temperature(20, TemperatureScale[0])
@pytest.mark.parametrize(
    "temp1, expected1",
    [
        (Temperature(10, TemperatureScale[2]), "461.67ºF"),
        (Temperature(50, TemperatureScale[1]), "-102.0ºF")
    ]
)
def test_substract(temp1, expected1):
    assert b.substract(temp1).ToString() == expected1

# Scenario 3, multiply
c = Temperature(30, TemperatureScale[1])
@pytest.mark.parametrize(
    "temp2, expected2",
    [
        (Temperature(100, TemperatureScale[2]), "-5194.5ºC"),
        (Temperature(78, TemperatureScale[0]), "766.8ºC")
    ]
)
def test_multiply(temp2, expected2):
    assert c.multiply(temp2).ToString() == expected2


# Scenario 4, divide
d = Temperature(40, TemperatureScale[1])
@pytest.mark.parametrize(
    "temp3, expected3",
    [
        (Temperature(50, TemperatureScale[1]), "0.8ºC"),
        (Temperature(100, TemperatureScale[0]), "1.06ºC")
    ]
)
def test_divdeBy(temp3, expected3):
    assert d.divideBy(temp3).ToString() == expected3
