from pickletools import pyset
import pytest

from KataTemp import Temperature
from KataTemp import TemperatureScale

# Testing conversion to Kelvin
@pytest.mark.parametrize(
    "test, expected",
    [
        (Temperature(20, TemperatureScale.Kelvin), 20.0),
        (Temperature(50, TemperatureScale.Fahrenheit), 283.15),
        (Temperature(100, TemperatureScale.Celsius), 373.15)
    ]
)
def test_toKelvin(test, expected):
    assert test.toKelvin().value == expected


# Testing conversion to Celsius
@pytest.mark.parametrize(
    "test, expected",
    [
        (Temperature(50, TemperatureScale.Kelvin), -223.15),
        (Temperature(35, TemperatureScale.Fahrenheit), 1.67),
        (Temperature(150, TemperatureScale.Celsius), 150)
    ]
)
def test_toCelsius(test, expected):
    assert test.toCelsius().value == expected


# Testing conversion to Fahrenheit
@pytest.mark.parametrize(
    "test, expected",
    [
        (Temperature(150, TemperatureScale.Kelvin), -189.67),
        (Temperature(40, TemperatureScale.Fahrenheit), 40.0),
        (Temperature(0, TemperatureScale.Celsius), 32.0)
    ]
)
def test_toFahrenheit(test, expected):
    assert test.toFahrenheit().value == expected

# Testing conversion to Fahrenheit
@pytest.mark.parametrize(
    "test, expected",
    [
        (Temperature(-60, TemperatureScale.Kelvin), "-60K"),
        (Temperature(43, TemperatureScale.Fahrenheit), "43F"),
        (Temperature(-5, TemperatureScale.Celsius), '-5C')
    ]
)
def test_ToString(test, expected):
    assert test.ToString() == expected

# Testing add
@pytest.mark.parametrize(
    "subject, predicate, expected",
    [
        (Temperature(-60, TemperatureScale.Kelvin), Temperature(50, TemperatureScale.Celsius), 263.15),
        (Temperature(85, TemperatureScale.Fahrenheit), Temperature(-98, TemperatureScale.Kelvin), -551.07),
        (Temperature(100, TemperatureScale.Celsius), Temperature(92, TemperatureScale.Fahrenheit), 133.33)
    ]
)
def test_add(subject, predicate, expected):
    assert subject.add(predicate).value == expected

# Testing diff
@pytest.mark.parametrize(
    "subject, predicate, expected",
    [
        (Temperature(100, TemperatureScale.Kelvin), Temperature(98, TemperatureScale.Celsius), -271.15),
        (Temperature(-85, TemperatureScale.Fahrenheit), Temperature(-50, TemperatureScale.Kelvin), 464.67),
        (Temperature(100, TemperatureScale.Celsius), Temperature(-100, TemperatureScale.Fahrenheit), 173.33)
    ]
)
def test_diff(subject, predicate, expected):
    assert subject.diff(predicate).value == expected

# Testing multiply
@pytest.mark.parametrize(
    "subject, predicate, expected",
    [
        (Temperature(8, TemperatureScale.Kelvin), Temperature(12, TemperatureScale.Kelvin), 96.0),
        (Temperature(71, TemperatureScale.Fahrenheit), Temperature(-3, TemperatureScale.Kelvin), -33019.97),
        (Temperature(30, TemperatureScale.Celsius), Temperature(2, TemperatureScale.Fahrenheit), -500.1)
    ]
)
def test_multiply(subject, predicate, expected):
    assert subject.multiply(predicate).value == expected

# Testing divide By
@pytest.mark.parametrize(
    "subject, predicate, expected",
    [
        (Temperature(30, TemperatureScale.Kelvin), Temperature(-273.15, TemperatureScale.Celsius), None),
        (Temperature(0, TemperatureScale.Fahrenheit), Temperature(-3, TemperatureScale.Kelvin), None)
    ]
)
def test_divideBy(subject, predicate, expected):
    assert subject.divideBy(predicate) == expected