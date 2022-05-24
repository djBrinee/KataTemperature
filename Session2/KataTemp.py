# Kata Temperature Excercise
# Author: Deivy Peña
# ID: 1099409
# Date: 5/24/2022
# Session No. 2

# Class to define scales

from pickletools import read_uint1


class TemperatureScale:
    Kelvin = "K"
    Celsius = "C"
    Fahrenheit = "F"

# Main class: Temperature

class Temperature:
    def __init__(self, value, scale = 'TemperatureScale'):
        self.value = value
        self.scale = scale

    # From any defined scale to Kelvin method
    def toKelvin(self):
        # If scale is Kelvin
        if(self.scale == 'K'):
            obValue = round(self.value, 2)
            object = Temperature(obValue, TemperatureScale.Kelvin)
            return object

        # If scale is Celsius 
        elif(self.scale == 'C'):
            obValue = round(self.value + 273.15, 2)
            object = Temperature(obValue, TemperatureScale.Kelvin)
            return object

        # If scale is Fahrenheit
        elif(self.scale == 'F'):
            obValue = round((self.value - 32) * 5/9 + 273.15, 2)
            object = Temperature(obValue, TemperatureScale.Kelvin)
            return object

    # From any defined scale to Fahrenheit method
    def toFahrenheit(self):
        # If scale is Kelvin
        if(self.scale == 'K'):
            obValue = round((self.value - 273.15) * 9/5 + 32, 2)
            object = Temperature(obValue, TemperatureScale.Fahrenheit)
            return object

        # If scale is Celsius 
        elif(self.scale == 'C'):
            obValue = round((self.value * 9/5) + 32, 2)
            object = Temperature(obValue, TemperatureScale.Fahrenheit)
            return object

        # If scale is Fahrenheit
        elif(self.scale == 'F'):
            obValue = round(self.value, 2)
            object = Temperature(obValue, TemperatureScale.Fahrenheit)
            return object

    # From any defined scale to Celsius method
    def toCelsius(self):
        # If scale is Kelvin
        if(self.scale == 'K'):
            obValue = round(self.value - 273.15, 2)
            object = Temperature(obValue, TemperatureScale.Celsius)
            return object

        # If scale is Celsius 
        elif(self.scale == 'C'):
            obValue = round(self.value, 2)
            object = Temperature(obValue, TemperatureScale.Celsius)
            return object

        # If scale is Fahrenheit
        elif(self.scale == 'F'):
            obValue = round((self.value - 32) * 5/9, 2)
            object = Temperature(obValue, TemperatureScale.Celsius)
            return object

        # ToString method (unifying value and scale)
        def ToString(self):
            return '{}{}'.format(self.value, self.scale)

    def ToString(self):
        return '{}{}'.format(self.value, self.scale)

    # Method to add
    def add(self, othertemp: 'Temperature'):
        # If scale is Kelvin
        if(self.scale == 'K'):
            obValue = round(self.value + othertemp.toKelvin().value, 2)
            if(obValue == 0):
                return None
            else:
                object = Temperature(obValue, TemperatureScale.Kelvin)
                return object

        # If scale is Celsius 
        elif(self.scale == 'C'):
            obValue = round(self.value + othertemp.toCelsius().value, 2)
            if(obValue == 0):
                return None
            else:
                object = Temperature(obValue, TemperatureScale.Celsius)
                return object

        # If scale is Fahrenheit
        elif(self.scale == 'F'):
            obValue = round(self.value + othertemp.toFahrenheit().value, 2)
            if(obValue == 0):
                return None
            else:
                object = Temperature(obValue, TemperatureScale.Fahrenheit)
                return object

    # Method to diff
    def diff(self, othertemp: 'Temperature'):
        # If scale is Kelvin
        if(self.scale == 'K'):
            obValue = round(self.value - othertemp.toKelvin().value, 2)
            if(obValue == 0):
                return None
            else:
                object = Temperature(obValue, TemperatureScale.Kelvin)
                return object

        # If scale is Celsius 
        elif(self.scale == 'C'):
            obValue = round(self.value - othertemp.toCelsius().value, 2)
            if(obValue == 0):
                return None
            else:
                object = Temperature(obValue, TemperatureScale.Celsius)
                return object

        # If scale is Fahrenheit
        elif(self.scale == 'F'):
            obValue = round(self.value - othertemp.toFahrenheit().value, 2)
            if(obValue == 0):
                return None
            else:
                object = Temperature(obValue, TemperatureScale.Fahrenheit)
                return object
    # Method to multiply
    def multiply(self, othertemp: 'Temperature'):
        # If scale is Kelvin
        if(self.scale == 'K'):
            obValue = round(self.value * othertemp.toKelvin().value, 2)
            if(obValue == 0):
                return None
            else:
                object = Temperature(obValue, TemperatureScale.Kelvin)
                return object

        # If scale is Celsius 
        elif(self.scale == 'C'):
            obValue = round(self.value * othertemp.toCelsius().value, 2)
            if(obValue == 0):
                return None
            else:
                object = Temperature(obValue, TemperatureScale.Celsius)
                return object

        # If scale is Fahrenheit
        elif(self.scale == 'F'):
            obValue = round(self.value * othertemp.toFahrenheit().value, 2)
            if(obValue == 0):
                return None
            else:
                object = Temperature(obValue, TemperatureScale.Fahrenheit)
                return object

    # Metgod to divde
    def divideBy(self, othertemp: 'Temperature'):
        # If scale is Kelvin
        if(self.scale == 'K'):
            if(othertemp.toKelvin().value == 0.0):
                return None
            else:
                obValue = round(self.value / othertemp.toKelvin().value, 2)
                # If division not defined
                if(obValue == 0):
                    return None
                else:
                    object = Temperature(obValue, TemperatureScale.Kelvin)
                    return object

        # If scale is Celsius 
        elif(self.scale == 'C'):
            if(othertemp.toCelsius().value == 0.0):
                return None
            else:
                obValue = round(self.value / othertemp.toKelvin().value, 2)
                # If division not defined
                if(obValue == 0):
                    return None
                else:
                    object = Temperature(obValue, TemperatureScale.Celsius)
                    return object

        # If scale is Fahrenheit
        elif(self.scale == 'F'):
            if(othertemp.toFahrenheit().value == 0.0):
                return None
            else:
                obValue = round(self.value / othertemp.toKelvin().value, 2)
                # If division not defined
                if(obValue == 0):
                    return None
                else:
                    object = Temperature(obValue, TemperatureScale.Fahrenheit)
                    return object

a = Temperature(60, TemperatureScale.Kelvin)
b = Temperature(-273.15, TemperatureScale.Celsius)

print(a.divideBy(b))


        
        


        

        



