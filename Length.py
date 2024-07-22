# Here is another module created by Length Module containing length related functions
# this module contains all functions related to the lengths given below
# km, meter, decimeter, centimeter, millimeter, micrometer, nanometer, picometer, miles, yard, foot, inch

class kilometer:
    kilometer = 0

    def __init__(self):
        pass
    
    def km2meter(self,km):
        self.kilometer = km * 1000
        return self.kilometer

    def km2dm(self,km):
        self.kilometer = km * 10000
        return self.kilometer

    def km2cm(self,km):
        self.kilometer = km * (10 ** 5)
        return self.kilometer

    def km2mm(self,km):
        self.kilometer = km * (10 ** 6)
        return self.kilometer

    def km2um(self,km):
        self.kilometer = km * (10 ** 9)
        return self.kilometer

    def km2nm(self,km):
        self.kilometer = km * (10 ** 12)
        return self.kilometer

    def km2pm(self,km):
        self.kilometer = km * (10 ** 15)
        return self.kilometer

    def km2miles(self,km):
        self.kilometer = km * 0.621
        return self.kilometer

    def km2foot(self,km):
        self.kilometer = km * 3280
        return self.kilometer

    def km2yard(self,km):
        self.kilometer = km  * 1093
        return self.kilometer

    def km2inches(self,km):
        self.kilometer = km * 39370
        return self.kilometer

class meter:
    meter = 0

    def __init__(self):
        pass

    def m2km(self,m):
        self.meter = m / 1000
        return self.meter

    def m2cm(self,m):
        self.meter = m * 100
        return self.meter

    def m2dm(self,m):
        self.meter = m * 10
        return self.meter

    def m2mm(self,m):
        self.meter = m * 1000
        return self.meter

    def m2um(self,m):
        self.meter = m * (10 ** 6)
        return self.meter

    def m2nm(self,m):
        self.meter = m * (10 ** 9)
        return self.meter

    def m2pm(self,m):
        self.meter = m * (10 ** 12)
        return self.meter

    def m2miles(self,m):
        self.meter = m * 0.00062
        return self.meter

    def m2yard(self,m):
        self.meter = m * 1.09
        return self.meter

    def m2foot(self,m):
        self.meter = m * 3.28
        return self.meter

    def m2inches(self,m):
        self.meter = m * 39.3
        return self.meter

class decimeter:
    decimeter = 0

    def __init__(self):
        pass

    def dm2km(self,dm):
        self.decimeter = dm / (10 ** 4)
        return self.decimeter

    def dm2m(self,dm):
        self.decimeter = dm / 10
        return self.decimeter

    def dm2cm(self,dm):
        self.decimeter = dm * 10
        return self.decimeter

    def dm2mm(self,dm):
        self.decimeter = dm * 100
        return self.decimeter

    def dm2um(self,dm):
        self.decimeter = dm * (10 ** 5)
        return self.decimeter

    def dm2nm(self,dm):
        self.decimeter = dm * (10 ** 8)
        return self.decimeter

    def dm2pm(self,dm):
        self.decimeter = dm * (10 ** 11)
        return self.decimeter

    def dm2miles(self,dm):
        self.decimeter = dm * (6.21371192 / (10 ** 5))
        return self.decimeter

    def dm2yard(self,dm):
        self.decimeter = dm * 0.1093
        return self.decimeter

    def dm2foot(self,dm):
        self.decimeter = dm * 0.3280
        return self.decimeter

    def dm2inches(self,dm):
        self.decimeter = dm * 3.937
        return self.decimeter

class centimeter:
    centimeter = 0

    def __init__(self,cm):
        self.centimeter = cm

    def cm2km(self):
        centimeter = self.centimeter / (10 ** 5)
        return centimeter

    def cm2m(self):
        centimeter = self.centimeter / 100
        return centimeter
    
    def cm2dm(self):
        centimeter = self.centimeter / 10
        return centimeter

    def cm2mm(self):
        centimeter = self.centimeter * 10
        return centimeter

    def cm2um(self):
        centimeter = self.centimeter * (10 ** 4)
        return centimeter

    def cm2nm(self):
        centimeter = self.centimeter * (10 ** 7)
        return centimeter

    def cm2pm(self):
        centimeter = self.centimeter * (10 ** 10)
        return centimeter

    def cm2miles(self):
        centimeter = self.centimeter * (6.21371192 / (10 ** 6))
        return centimeter

    def cm2yard(self):
        centimeter = self.centimeter * 0.01093
        return centimeter

    def cm2foot(self):
        centimeter = self.centimeter * 0.03280
        return centimeter

    def cm2inches(self):
        centimeter = self.centimeter * 0.3937
        return centimeter

class millimeter:
    millimeter = 0

    def __init__(self,mm):
        self.millimeter = mm

    def mm2km(self):
        millimeter = self.millimeter / (10 ** 6)
        return millimeter

    def mm2m(self):
        millimeter = self.millimeter / 1000
        return millimeter

    def mm2cm(self):
        millimeter = self.millimeter / 10
        return millimeter

    def mm2um(self):
        millimeter = self.millimeter * 1000
        return millimeter

    def mm2nm(self):
        millimeter = self.millimeter * (10 ** 6)
        return millimeter

    def mm2pm(self):
        millimeter = self.millimeter * (10 ** 9)
        return millimeter

    def mm2miles(self):
        millimeter = self.millimeter * (6.21371192 / (10 ** 7))
        return millimeter

    def mm2yard(self):
        millimeter = self.millimeter * 0.00109
        return millimeter

    def mm2foot(self):
        millimeter = self.millimeter * 0.00328
        return millimeter

    def mm2inches(self):
        millimeter = self.millimeter * 0.0393
        return millimeter

class micrometer:
    micrometer = 0

    def __init__(self,um):
        self.micometer = um

    def um2km(self):
        micrometer = self.micrometer / (10 ** 9)
        return micrometer

    def um2m(self):
        micrometer = self.micrometer / (10 ** 6)
        return micrometer

    def um2cm(self):
        micrometer = self.micrometer / (10 ** 4)
        return micrometer

    def um2dm(self):
        micrometer = self.micrometer / (10 ** 5)
        return micrometer

    def um2mm(self):
        micrometer = self.micrometer / 1000
        return micrometer

    def um2nm(self):
        micrometer = self.micrometer * 1000
        return micrometer

    def um2pm(self):
        micrometer = self.micrometer * (10 ** 6)
        return micrometer

    def um2miles(self):
        micrometer = self.micrometer * (6.21371192 / (10 ** 10))
        return micrometer

    def um2yard(self):
        micrometer = self.micrometer * (1.0936133 / (10 ** 6))
        return micrometer

    def um2foot(self):
        micrometer = self.micrometer * (3.2808399 / (10 ** 6))
        return micrometer

    def um2inches(self):
        micrometer = self.micrometer * (3.93700787 / (10 ** 5))
        return micrometer

class nanometer:
    nanometer = 0

    def __init__(self,nm):
        self.nanometer = nm

    def nm2km(self):
        nanometer = self.nanometer / (10 ** 12)
        return nanometer

    def nm2m(self):
        nanometer = self.nanometer / (10 ** 9)
        return nanometer

    def nm2cm(self):
        nanometer = self.nanometer / (10 ** 7)
        return nanometer

    def nm2dm(self):
        nanometer = self.nanometer / (10 ** 8)
        return nanometer

    def nm2mm(self):
        nanometer = self.nanometer / (10 ** 6)
        return nanometer

    def nm2um(self):
        nanometer = self.nanometer / 1000
        return nanometer

    def nm2pm(self):
        nanometer = self.nanometer * 1000
        return nanometer

    def nm2miles(self):
        nanometer = self.nanometer * (6.21371192 / (10 ** 13))
        return nanometer

    def nm2yard(self):
        nanometer = self.nanometer * (1.0936133 / (10 ** 9))
        return nanometer

    def nm2foot(self):
        nanometer = self.nanometer * (3.2808399 / (10 ** 9))
        return nanometer

    def nm2inches(self):
        nanometer = self.nanometer * (3.93700787 / (10 ** 8))
        return nanometer

class picometer:
    picometer = 0

    def __init__(self,pm):
        self.picometer = pm

    def pm2km(self):
        picometer = self.picometer / (10 ** 15)
        return picometer

    def pm2m(self):
        picometer = self.picometer / (10 ** 12)
        return picometer

    def pm2cm(self):
        picometer = self.picometer / (10 ** 10)
        return picometer

    def pm2dm(self):
        picometer = self.picometer / (10 ** 11)
        return picometer

    def pm2mm(self):
        picometer = self.picometer / (10 ** 9)
        return picometer

    def pm2um(self):
        picometer = self.picometer / (10 ** 6)
        return picometer

    def pm2nm(self):
        picometer = self.picometer / 1000
        return picometer

    def pm2miles(self):
        picometer = self.picometer * (6.21371192 / (10 ** 16))
        return picometer

    def pm2yard(self):
        picometer = self.picometer * (1.0936133 / (10 ** 12))
        return picometer

    def pm2foot(self):
        picometer = self.picometer * (3.2808399 / (10 ** 12))
        return picometer

    def pm2inches(self):
        picometer = self.picometer * (3.93700787 / (10 ** 11))
        return picometer

class mile:
    mile = 0

    def __init__(self,ml):
        self.mile = ml

    def mile2km(self):
        mile = self.mile * 1.609344
        return mile

    def mile2m(self):
        mile = self.mile * 1609
        return mile

    def mile2cm(self):
        mile = self.mile * 160934
        return mile
    
    def mile2dm(self):
        mile = self.mile * 16093
        return mile

    def mile2mm(self):
        mile = self.mile * 1609344
        return mile

    def mile2um(self):
        mile = self.mile * (1609344 * (10 ** 9))
        return mile

    def mile2nm(self):
        mile = self.mile * (1609344 * (10 ** 12))
        return mile
    
    def mile2pm(self):
        mile = self.mile * (1609344 * (10 ** 15))
        return mile

    def mile2yard(self):
        mile = self.mile * 1760
        return mile
    
    def mile2foot(self):
        mile = self.mile * 5280
        return mile
    
    def mile2inche(self):
        mile = self.mile * 63360
        return mile

class yard:
    yard = 0

    def __init__(self,yd):
        self.yard = yd

    def yd2km(self):
        yard = self.yard * 0.000914
        return yard

    def yd2m(self):
        yard = self.yard * 0.9144
        return yard

    def yd2cm(self):
        yard = self.yard * 91
        return yard

    def yd2dm(self):
        yard = self.yard * 9.1
        return yard

    def yd2mm(self):
        yard = self.yard * 914
        return yard
    
    def yd2um(self):
        yard = self.yard * 914400
        return yard

    def yd2nm(self):
        yard = self.yard * (9144 * (10 ** 5))
        return yard
    
    def yd2pm(self):
        yard = self.yard * (9144 * (10 ** 11))
        return yard

    def yd2mile(self):
        yard = self.yard * 0.00056
        return yard

    def yd2foot(self):
        yard = self.yard * 3
        return yard

    def yd2inches(self):
        yard = self.yard * 36
        return yard

class Foot:
    Foot = 0

    def __init__(self,ft):
        self.Foot = ft

    def ft2km(self):
        Foot = self.Foot * 0.0003
        return Foot

    def ft2m(self):
        Foot = self.Foot * 0.304
        return Foot

    def ft2cm(self):
        Foot = self.Foot * 30
        return Foot
    
    def ft2dm(self):
        Foot = self.Foot * 3.048
        return Foot

    def ft2mm(self):
        Foot = self.Foot * 304
        return Foot

    def ft2um(self):
        Foot = self.Foot * 304800
        return Foot

    def ft2nm(self):
        Foot = self.Foot * (3048 * (10 ** 5))
        return Foot

    def ft2pm(self):
        Foot = self.Foot * (3048 * (10 ** 11))
        return Foot

    def ft2mile(self):
        Foot = self.Foot * 0.00018
        return Foot

    def ft2yard(self):
        Foot = self.Foot * 0.33
        return Foot

    def ft2inches(self):
        Foot = self.Foot * 12
        return Foot

class Inch:
    Inch = 0

    def __init__(self,inch):
        self.Inch = inch

    def inch2km(self):
        Inch = self.Inch * (2.54 / (10 ** 5))
        return Inch

    def inch2m(self):
        Inch = self.Inch * 0.0254
        return Inch

    def inch2cm(self):
        Inch = self.Inch * 2.54
        return Inch

    def inch2dm(self):
        Inch = self.Inch * 0.254
        return Inch

    def inch2mm(self):
        Inch = self.Inch * 25.4
        return Inch

    def inch2um(self):
        Inch = self.Inch * 25400
        return Inch

    def inch2nm(self):
        Inch = self.Inch * (254 * (10 ** 5))
        return Inch

    def inch2pm(self):
        Inch = self.Inch * (254 * (10 ** 10))
        return Inch

    def inch2yard(self):
        Inch = self.Inch * 0.027
        return Inch

    def inch2mile(self):
        Inch = self.Inch * (1.57828283 * (10 ** 5))
        return Inch

    def inch2foot(self):
        Inch = self.Inch * 0.083
        return Inch