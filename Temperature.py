# Here is another conversion units of temperature related
# Following units are envolved here
# Celsius, Fahrenheit, Kelvin, Rankine, reaumur

class celsius:
    celsius = 0

    def __init__(self,C):
        self.celsius = C

    def c2F(self):
        celsius = (self.celsius * 1.8) + 32
        return celsius

    def c2k(self):
        celsius = self.celsius + 273.15
        return celsius

    def c2rrankine(self):
        celsius = ((self.celsius * 1.8) + 32) + 459.67
        return celsius

    def c2reaumur(self):
        celsius = self.celsius * 0.8
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