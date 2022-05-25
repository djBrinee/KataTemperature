import pytest

from KataTemp import Temperature
from KataTemp import TemperatureScale

# Testing to Kelvin conversion

@pytest.mark.parametrize(
    "test, expected",
    [
        (Temperature(52, TemperatureScale.Celsius), 325.15),
        (Temperature(-60, TemperatureScale.Kelvin), -60.0 ),
        (Temperature(100, TemperatureScale.Fahrenheit), 310.93 )
    ]
)
def test_toKelvin(test, expected):
    assert test.toKelvin().value == expected


# Testing to Celsius conversion

@pytest.mark.parametrize(
    "test, expected",
    [
        (Temperature(-30, TemperatureScale.Celsius), -30.0),
        (Temperature(50, TemperatureScale.Kelvin), -223.15 ),
        (Temperature(50, TemperatureScale.Fahrenheit), 10.0 )
    ]
)
def test_toCelsius(test, expected):
    assert test.toCelsius().value == expected


# Testing to Fahrenheit conversion

@pytest.mark.parametrize(
    "test, expected",
    [
        (Temperature(150, TemperatureScale.Celsius), 305.0),
        (Temperature(-80, TemperatureScale.Kelvin), -603.67 ),
        (Temperature(20, TemperatureScale.Fahrenheit), 20.0 )
    ]
)
def test_toFahrenheit(test, expected):
    assert test.toFahrenheit().value == expected


# Testing to String function
@pytest.mark.parametrize(
    "test, expected",
    [
        (Temperature(150, TemperatureScale.Celsius), '150C'),
        (Temperature(-80, TemperatureScale.Kelvin), '-80K' ),
        (Temperature(20, TemperatureScale.Fahrenheit), '20F' )
    ]
)
def test_toString(test, expected):
    assert test.toString() == expected


# Testing add operation
@pytest.mark.parametrize(
    "term1, term2, result",
    [
        (Temperature(150, TemperatureScale.Celsius), Temperature(30, TemperatureScale.Fahrenheit), 148.89),
        (Temperature(-80, TemperatureScale.Fahrenheit), Temperature(30, TemperatureScale.Kelvin), -485.67),
        (Temperature(-50, TemperatureScale.Kelvin), Temperature(100, TemperatureScale.Celsius), 323.15),
    ]
)
def test_add(term1, term2, result):
    assert term1.add(term2).value == result


# Testing diff operation
@pytest.mark.parametrize(
    "term1, term2, result",
    [
        (Temperature(500, TemperatureScale.Celsius), Temperature(100, TemperatureScale.Fahrenheit), 462.22),
        (Temperature(-800, TemperatureScale.Fahrenheit), Temperature(30, TemperatureScale.Kelvin), -394.33),
        (Temperature(100, TemperatureScale.Kelvin), Temperature(-30, TemperatureScale.Celsius), -143.15)
    ]
)
def test_diff(term1, term2, result):
    assert term1.diff(term2).value == result


# Testing multiply operation
@pytest.mark.parametrize(
    "term1, term2, result",
    [
        (Temperature(50, TemperatureScale.Celsius), Temperature(3, TemperatureScale.Fahrenheit), -805.5),
        (Temperature(25, TemperatureScale.Fahrenheit), Temperature(80, TemperatureScale.Kelvin), -7891.75),
        (Temperature(60, TemperatureScale.Kelvin), Temperature(-25, TemperatureScale.Celsius), 14889.0)
    ]
)
def test_multiply(term1, term2, result):
    assert term1.multiply(term2).value == result

# Testing unwanted cases to division operation

@pytest.mark.parametrize(
    "term1, term2",
    [
        (Temperature(50, TemperatureScale.Celsius), Temperature(32, TemperatureScale.Fahrenheit)),
        (Temperature(0, TemperatureScale.Fahrenheit), Temperature(80, TemperatureScale.Kelvin))
    ]
)
def test_divideBy(term1, term2):
    assert term1.divideBy(term2) == None

