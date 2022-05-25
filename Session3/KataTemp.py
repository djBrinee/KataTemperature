# Demostrating knowledge aboyt homework: Kata Teperarature.
# Author: Deivy Jr. Peña Rodríguez.
# ID: 1099429.
# Session No. 3
# Date 5/25/2022


# Class to define scales

class TemperatureScale:
    Kelvin = 'K'
    Celsius = 'C'
    Fahrenheit = 'F'

# Main CLass: Temperature
class Temperature:

    #atributes of the class
    def __init__(self, value, scale: 'TemperatureScale'):
        self.value = value
        self.scale = scale

    # Function to convert from any scale to Kelvin

    def toKelvin(self):
        if(self.scale == 'K'):
            a = Temperature(round(self.value, 2), TemperatureScale.Kelvin)
        elif(self.scale == 'C'):
            a = Temperature(round(self.value + 273.15, 2), TemperatureScale.Kelvin)
        elif(self.scale == 'F'):
            a = Temperature(round((self.value - 32) * 5/9 + 273.15, 2), TemperatureScale.Kelvin)
        else:
            a = None
        return a
    
    # Function to convert from any scale to Celsius
    def toCelsius(self):
        if(self.scale == 'K'):
            a = Temperature(round(self.value - 273.15, 2), TemperatureScale.Celsius)
        elif(self.scale == 'C'):
            a = Temperature(round(self.value, 2), TemperatureScale.Celsius)
        elif(self.scale == 'F'):
            a = Temperature(round((self.value - 32) * 5/9, 2), TemperatureScale.Celsius)
        else:
            a = None
        return a

    # Function to convert from any scale to Fahrenheit
    def toFahrenheit(self):
        if(self.scale == 'K'):
            a = Temperature(round((self.value - 273.15) * 9/5 + 32, 2), TemperatureScale.Celsius)
        elif(self.scale == 'C'):
            a = Temperature(round((self.value * 9/5) + 35, 2), TemperatureScale.Celsius)
        elif(self.scale == 'F'):
            a = Temperature(round(self.value, 2), TemperatureScale.Celsius)
        else:
            a = None
        return a

    #Function to return string with class value and scale
    def toString(self):
        return '{}{}'.format(self.value, self.scale)


    # Function to add operation
    def add(self, other: 'Temperature'):
        if(self.scale == 'K'):
            a = Temperature(round((self.value + other.toKelvin()), 2), TemperatureScale.Kelvin)
        elif(self.scale == 'C'):
            a = Temperature(round((self.value + other.toCelsius()), 2), TemperatureScale.Celsius)
        elif(self.scale == 'F'):
            a = Temperature(round((self.value + other.toFahrenheit()), 2), TemperatureScale.Fahrenheit)
        if(a.value == 0.0):
            result = None
        else:
            result = a
        return result

    # function to diff operation
    def diff(self, other: 'Temperature'):
        if(self.scale == 'K'):
            a = Temperature(round((self.value - other.toKelvin()), 2), TemperatureScale.Kelvin)
        elif(self.scale == 'C'):
            a = Temperature(round((self.value - other.toCelsius()), 2), TemperatureScale.Celsius)
        elif(self.scale == 'F'):
            a = Temperature(round((self.value - other.toFahrenheit()), 2), TemperatureScale.Fahrenheit)
        if(a.value == 0.0):
            result = None
        else:
            result = a
        return result

    # Function to multiply operation
    def multiply(self, other: 'Temperature'):
        if(self.scale == 'K'):
            a = Temperature(round((self.value * other.toKelvin()), 2), TemperatureScale.Kelvin)
        elif(self.scale == 'C'):
            a = Temperature(round((self.value * other.toCelsius()), 2), TemperatureScale.Celsius)
        elif(self.scale == 'F'):
            a = Temperature(round((self.value * other.toFahrenheit()), 2), TemperatureScale.Fahrenheit)
        if(a.value == 0.0):
            result = None
        else:
            result = a
        return result

    # Function to divide operation
    def divdeBy(self, other: 'Temperature'):
        if(self.scale == 'K'):
            if(other.toKelvin() == 0):
                a = None
            else:
                a = Temperature(round((self.value / other.toKelvin()), 2), TemperatureScale.Kelvin)
        elif(self.scale == 'C'):
            if(other.toCelsius() == 0):
                a = None
            else:
                a = Temperature(round((self.value / other.toCelsius()), 2), TemperatureScale.Celsius)
        elif(self.scale == 'F'):
            if(other.tofahrenheit() == 0):
                a = None
            else:
                a = Temperature(round((self.value / other.tofahrenheit()), 2), TemperatureScale.Fahrenheit)
        if(a.value == 0.0):
            result = None
        else:
            result = a
        return result