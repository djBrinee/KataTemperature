# API about Temperature to demostrate the abitilies through Kata Ex.
# Nombre: Deivy Jr. Peña Rodríguez.
# ID: 1099429.
# Session 1

TemperatureScale = ["Fahrenheit", "Celsius", "Kelvin"]

# Main Class
class Temperature:
    # Defining attributes
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale
    
    # Defining Class Methods

    # Function con convert from any of defined scales to Kelvin
    def toKelvin(self):
        if(self.scale == "Kelvin"):
            return round(self.value, 2)
        elif(self.scale == "Fahrenheit"):
            return round(((self.value - 32) * 5/9 + 273.15), 2)
        elif(self.scale == "Celsius"):
            return round(self.value + 273.15, 2)
        else:
            None
    
    # Function con convert from any of defined scales to Celsius
    def toCelsius(self):
        if(self.scale == "Kelvin"):
            return round(self.value - 273.15, 2)
        elif(self.scale == "Fahrenheit"):
            return round((self.value - 32) * 5/9, 2)
        elif(self.scale == "Celsius"):
            return round(self.value, 2)
        else:
            None
    # Function con convert from any of defined scales to Fahrenheit
    def toFahrenheit(self):
        if(self.scale == "Kelvin"):
            return round((self.value - 273.15) * 9/5 + 32, 2)
        elif(self.scale == "Fahrenheit"):
            return round(self.value, 2)
        elif(self.scale == "Celsius"):
            return round((self.value * 9/5) + 32, 2)
        else:
            None


    # Function to add the object with another object (it values)
    def add(self, othertemp: 'Temperature'):

        if(self.scale == "Kelvin"):
            a = Temperature(round(self.value + othertemp.toKelvin(), 2), TemperatureScale[2])
        elif(self.scale == "Fahrenheit"):
            a = Temperature(round(self.value + othertemp.toFahrenheit(), 2), TemperatureScale[0])
        elif(self.scale == "Celsius"):
            a = Temperature(round(self.value + othertemp.toCelsius(), 2), TemperatureScale[1])
        else:
            a = None
        if(a == None or a.value == 0):
            return a
        else:
            return a

    # Function to substract the object with another object (it values)
    def substract(self, othertemp: 'Temperature'):

        if(self.scale == "Kelvin"):
            a = Temperature(round(self.value - othertemp.toKelvin(), 2), TemperatureScale[2])
        elif(self.scale == "Fahrenheit"):
            a = Temperature(round(self.value - othertemp.toFahrenheit(), 2), TemperatureScale[0])
        elif(self.scale == "Celsius"):
            a = Temperature(round(self.value - othertemp.toCelsius(), 2), TemperatureScale[1])
        else:
            a = None
        if(a == None or a.value == 0):
            a = None
        return a

    # Function to multiply the object with another object (it values)
    def multiply(self, othertemp: 'Temperature'):
        if(self.scale == "Kelvin"):
            a = Temperature(round(self.value * othertemp.toKelvin(), 2), TemperatureScale[2])
        elif(self.scale == "Fahrenheit"):
            a = Temperature(round(self.value * othertemp.toFahrenheit(), 2), TemperatureScale[0])
        elif(self.scale == "Celsius"):
            a = Temperature(round(self.value * othertemp.toCelsius(), 2), TemperatureScale[1])
        else:
            a = None
        if(a == None or a.value == 0):
            a = None
        return a

    # Function to divide the object with another object (it values)
    def divideBy(self, othertemp: 'Temperature'):
        if(othertemp.value == 0):
            return None
        else:
            if(self.scale == "Kelvin"):
                a = Temperature(round(self.value / othertemp.toKelvin(), 2), TemperatureScale[2])
            elif(self.scale == "Fahrenheit"):
                a = Temperature(round(self.value / othertemp.tofahrenheit(), 2), TemperatureScale[0])
            elif(self.scale == "Celsius"):
                a = Temperature(round(self.value / othertemp.toCelsius(), 2), TemperatureScale[1])
            else:
                a = None
            if(a == None or a.value == 0):
                a = None
            return a
            
    # Function to show objects value and scale in a string
    def ToString(self):
        return '{}º{}'.format(self.value, self.scale[0])


