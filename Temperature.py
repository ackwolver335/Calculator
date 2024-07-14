# Here is another conversion units of temperature related
# Following units are envolved here
# Celsius, Fahrenheit, Kelvin, Rankine, reaumur

# It contains different methods regariding the calculation of temperature in different available units
# further description is been given below regarding the code and method's explanation

"""---- Main File contains the Methods or Functions that are mentioned below ! -----"""

celsius_methods = [
    '__init__(self)',
    'c2F(self,value)',
    'c2k(self,value)',
    'c2rrankine(self,value)',
    'c2reaumur'
]

class celsius:
    celsius = 0

    # ------------ Initial Methods for initiating objects and their overview on different available methods ------------------
    # ------------------------------------------------------------------------------------------------------------------------
    # This Module together with the intial one have its overall proper data over to the Github : @ackwolver335 ---------------

    def __init__(self):
        """
            :: Temperature Module ::

            Class : celsius
            Function : __init__(self) it don't contains different arguments at its initial phase
            We are getting the data at the runtime of the Program.

            Also the available data members of this one is explained below :
            1. celsius : This is generally used in order to store the value after getting converted in the required unit in Temperature.

            Temperature Module -> Designed by Abhay Chaudhary.
        """

        # Here we have a general use of pass keyword as we don't have further code in __init__() method.
        pass

    def c2F(self,value):

        """
            :: Temperature Module ::

            Class : celsius
            Function : c2F(self,value) in general for conversion of one unit into another, we uses this value.

            Arguments :
            value : It stands for the value of celsius to be converted into Fahrenheit Temperature Unit.

            Temperature Module -> Designed by Abhay Chaudhary
        """

        # main source code for conversion of units
        # contains the formula for conversion of celsius into Fahrenheit Unit

        celsius = (value * 1.8) + 32
        return celsius

    def c2k(self,value):

        """
            :: Temperature Module ::

            Class : celsius
            Function : c2k(self,value) in general for conversion of celsius into kelvin temperature with the use of this value.

            Arguments :
            1. value : It is the main source value regarding the conversion.

            Temperature Module -> Designed by Abhay Chaudhary.
        """

        # main source code for conversion of units
        # contains the formula for conversion of celsius into kelvin unit

        celsius = value + 273.15
        return celsius

    def c2rrankine(self,value):

        """
            :: Temperature Module ::

            Class : celsius
            Function : c2rrankine(self,value), it contains value argument and self for conversion of temperature into rankine unit.

            Arguments :
            1. value : It is the value of celsius used for conversion into kelvin unit.

            Temperature Module -> Designed by Abhay Chaudhary.
        """

        # main source code for conversion of units
        # contains the formula for conversion of celsius unit into rankine unit

        celsius = ((value * 1.8) + 32) + 459.67
        return celsius

    def c2reaumur(self,value):

        """
            :: Temperature Module ::

            Class : celsius
            Function : c2reaumur(self,value) its main purpose is to convert the celsius temperature unit into reaumur unit.

            Arguments :
            1. value : It is the value of celsius used for conversion into reaumur units.

            Temperature Module -> Designed by Abhay Chaudhary.
        """

        # main source code for conversion of units
        # contains the formula for conversion of celsius unit into reaumur unit

        celsius = value * 0.8
        return celsius

class Fahrenheit:
    fahrenheit = 0

    def __init__(self,F):
        self.fahrenheit = F

    def f2c(self):
        fahrenheit = (self.fahrenheit - 32) / 1.8
        return fahrenheit

    def f2k(self):
        fahrenheit = (self.fahrenheit + 459) / 1.8
        return fahrenheit

    def f2rankine(self):
        fahrenheit = self.fahrenheit + 459
        return fahrenheit

    def fsreaumur(self):
        fahrenheit = (self.fahrenheit - 32) / 2.25
        return fahrenheit

class Kelvin:
    kelvin = 0

    def __init__(self,k):
        self.kelvin = k

    def k2F(self):
        kelvin = (self.kelvin * 1.8) - 459
        return kelvin

    def k2c(self):
        kelvin = self.kelvin - 273.15
        return kelvin

    def k2rankine(self):
        kelvin = self.kelvin * 1.8
        return kelvin

    def k2reaumur(self):
        kelvin = (self.kelvin - 273.15) * 0.8
        return kelvin

class Rankine:
    rankine = 0

    def __init__(self,rank):
        self.rankine = rank

    def rank2F(self):
        rankine = self.rankine - 459
        return rankine
    
    def rank2C(self):
        rankine = ((self.rankine - 32) - 459) / 1.8
        return rankine

    def rank2k(self):
        rankine = self.rankine / 1.8
        return rankine

    def rank2reaumur(self):
        rankine = ((self.rankine - 32) - 459) / 2.25
        return rankine

class Reaumur:
    reaumur = 0

    def __init__(self,reaum):
        self.reaumur = reaum

    def reaum2F(self):
        reaumur = (self.reaumur * 2.25) + 32
        return reaumur

    def reaum2C(self):
        reaumur = self.reaumur * 1.25
        return reaumur

    def reaum2K(self):
        reaumur = (self.reaumur * 1.25) + 273.15
        return reaumur

    def reaum2rank(self):
        reaumur = ((self.reaumur * 2.25) + 32) + 459
        return reaumur