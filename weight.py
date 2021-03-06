# Here is the Program which contain the function of weight converting in it differently
# This Module contains the functions in classes of these weights units
# kg, g, tonne, milligm, microgm, pound, quintal, ounze, carat, grain, stone, dram

# Let us start making the functions
# Here I have created a class for all kilogram conversion functions

# here is the KG Class

class kilogram:
    kilogram = None

    def __init__(self,kg):
        self.kilogram = kg

    def kg2g(self):                        
        gram = self.kilogram * 1000
        return gram

    def kg2milligm(self):                  
        milligm = self.kilogram * (10 ** 6)
        return milligm

    def kg2microgm(self):                  
        microgm = self.kilogram * (10 ** 9)
        return microgm

    def kg2tonne(self):                    
        tonne = self.kilogram / 1000
        return tonne

    def kg2quintal(self):                  
        quintal = self.kilogram / 100
        return quintal

    def kg2pound(self):                    
        pound = self.kilogram * 2.2
        return pound

    def kg2ounce(self):                    
        ounce = self.kilogram * 35.2
        return ounce

    def kg2carat(self):                    
        carat = self.kilogram * 5000
        return carat

    def kg2grain(self):                    
        grain = self.kilogram * 15432
        return grain

    def kg2st(self):                       
        stone = self.kilogram * 0.15
        return stone

    def kg2dr(self):                       
        dram = self.kilogram * 564
        return dram

# Here I have created a gram class similar to that of kilogram'e one

class gram:
    gram = 0

    def __init__(self,g):
        self.gram = g

    def g2tonne(self):                      
        tonne = self.gram / (10 ** 6)
        return tonne

    def g2kg(self):                         
        kg = self.gram / 1000
        return kg

    def g2mg(self):                         
        mg = self.gram * 1000
        return mg

    def g2microg(self):                     
        microgm = self.gram * (10 ** 6)
        return microgm

    def g2quintal(self):                    
        quintal = self.gram / (10 ** 5)
        return quintal

    def g2pound(self):                      
        pound = self.gram * 0.0022
        return pound

    def g2ounce(self):                      
        ounce = self.gram * 0.035
        return ounce

    def g2carat(self):                      
        carat = self.gram * 5
        return carat

    def g2grain(self):                      
        grain = self.gram * 15.4
        return grain

    def g2stone(self):                      
        stone = self.gram * 0.00015
        return stone

    def g2dram(self):                       
        dram = self.gram * 0.5643
        return dram

# Here are the tonne conversion functions containing classes

class tonne:
    tonne = 0

    def __init__(self,ton):
        self.tonne = ton

    def tonne2kg(self):
        kg = self.tonne * 1000
        return kg

    def tonne2g(self):
        g  = self.tonne * (10 ** 6)
        return g

    def tonne2milligm(self):
        milligm = self.tonne * (10 ** 9)
        return milligm

    def tonne2microgm(self):
        microgm = self.tonne * (10 ** 12)
        return microgm

    def tonne2quintal(self):
        quintal = self.tonne * 10
        return quintal

    def tonne2pound(self):
        pound = self.tonne * 2.204
        return pound

    def tonne2ounce(self):
        ounce = self.tonne * 35273
        return ounce

    def tonne_to_carat(tonne):
        carat = tonne * (5 * (10 ** 6))
        return carat

    def tonne2grain(self):
        grain = self.tonne * 15432358
        return grain

    def tonne2stone(self):
        stone = self.tonne * 160
        return stone

    def tonne2dram(self):
        dram = self.tonne * 573440
        return dram

# Here are the milligm conversion classes

class milligm:
    milligm = 0

    def __init_(self,mlgm):
        self.milligm = mlgm

    def milligm2tonne(self):
        tonne = self.milligm / (10 ** 9)
        return tonne

    def milligm2kg(self):
        kg = self.milligm / (10 ** 6)
        return kg

    def milligm2g(self):
        g = self.milligm / 1000
        return g

    def milligm2micro(self):
        micro_gm = self.milligm * 1000
        return micro_gm

    def milligm2quintal(self):
        quintal = self.milligm / (10 ** 8)
        return quintal

    def milligm2pound(self):
        pound = self.milligm * 2.204622
        return pound

    def milligm2ounze(self):
        ounze = self.milligm * 3.527396
        return ounze

    def milligm2carat(self):
        carat = self.milligm * 0.005
        return carat

    def milligm2grain(self):
        grain = self.milligm * 0.0154323
        return grain

    def milligm2stone(self):
        stone = self.milligm * 1.57473044
        return stone

    def milligm2dram(self):
        dram = self.milligm * 0.000564383
        return dram

# here is another class of microgram

class microgram:
    microgm = 0

    def __init__(self,mcgm):
        self.microgm = mcgm

    def microgm2tonne(self):
        tonne = self.microgm / (10 ** 12)
        return tonne

    def microgm2kg(self):
        kilogm = self.microgm / (10 ** 9)
        return kilogm

    def microgm2g(self):
        gram = self.microgm / (10 ** 6)
        return gram

    def microgm2milligm(self):
        milligm = self.microgm * 1000
        return milligm

    def microgm2quintal(self):
        quital = self.microgm / (10 ** 11)
        return quital

    def microgm2pound(self):
        pound = self.microgm * 2.20462262
        return pound

    def microgm2ounze(self):
        ounze = self.microgm * 3.52739619
        return ounze

    def microgm2carat(self):
        carat = self.microgm / (5 * (10 ** 6))
        return carat

    def microgm2grain(self):
        grain = self.microgm * 1.54323584
        return grain

    def microgm2stone(self):
        stone = self.microgm * (1.57473044 / (10 ** 10))
        return stone

    def microgm2dram(self):
        dram = self.microgm * (5.64383391 / (10 ** 7))
        return dram

# here is the Pound Class

class pound:
    pound = 0

    def __init__(self,pd):
        self.pound = pd

    def pd2kg(self):
        pound = self.pound * 0.453
        return pound

    def pd2g(self):
        pound = self.pound * 453
        return pound

    def pd2tonne(self):
        pound = self.pound * (453 / (10 ** 5))
        return pound

    def pd2milligm(self):
        pound = self.pound * 453592
        return pound

    def pd2microgm(self):
        pound = self.pound * 453592370
        return pound

    def pd2quintal(self):
        pound = self.pound * (453 / (10 ** 3))
        return pound

    def pd2ounze(self):
        pound = self.pound * 16
        return pound

    def pd2carat(self):
        pound = self.pound * 2267
        return pound

    def pd2grain(self):
        pound = self.pound * 7000
        return pound

    def pd2stone(self):
        pound = self.pound * (714 / (10 ** 2))
        return pound

    def pd2dram(self):
        pound = self.pound * 256
        return pound

# here is the Quintal Class

class quintal:
    quintal = 0

    def __init__(self,qtal):
        self.quintal = qtal

    def qn2tonne(self):
        quintal = self.quintal * 0.1
        return quintal

    def qn2kg(self):
        quintal = self.quintal * 100
        return quintal

    def qn2g(self):
        quintal = self.quintal * (10 ** 5)
        return quintal

    def qn2pound(self):
        quintal = self.quintal * 220.46
        return quintal

    def qn2milligm(self):
        quintal = self.quintal * (10 ** 8)
        return quintal

    def qn2microgm(self):
        quintal = self.quintal * (10 ** 11)
        return quintal

    def qn2ounze(self):
        quintal = self.quintal * 3527
        return quintal

    def qn2carat(self):
        quintal = self.quintal * (5 * (10 ** 5))
        return quintal

    def qn2grain(self):
        quintal = self.quintal * 1543235
        return quintal

    def qn2stone(self):
        quintal = self.quintal * 15.74
        return quintal

    def qn2dram(self):
        quintal = self.quintal * 56438
        return quintal

# here is the ounce Class

class ounze:
    ounze = 0

    def __init__(self,oz):
        self.ounze = oz

    def oz2tonne(self):
        ounze = self.ounze * 2.83
        return ounze

    def oz2kg(self):
        ounze = self.ounze * 0.028
        return ounze

    def oz2g(self):
        ounze = self.ounze * 28
        return ounze

    def oz2pound(self):
        ounze = self.ounze * 0.0625
        return ounze

    def oz2quintal(self):
        ounze = self.ounze * (283 / (10 ** 3))
        return ounze

    def oz2milligm(self):
        ounze = self.ounze * 28349
        return ounze

    def oz2microgm(self):
        ounze = self.ounze * 28349523
        return ounze

    def oz2carat(self):
        ounze = self.ounze * 141
        return ounze

    def oz2grain(self):
        ounze = self.ounze * 437
        return ounze

    def oz2stone(self):
        ounze = self.ounze * (446 / (10 ** 3))
        return ounze

    def oz2dram(self):
        ounze = self.ounze * 16
        return ounze

# here is the carat Class

class carat:
    carat = 0

    def __init__(self,ct):
        self.carat = ct

    def ct2tonne(self):
        carat = self.carat * (2 / (10 ** 7))
        return carat

    def ct2kg(self):
        carat = self.carat * (2 / (10 ** 4))
        return carat

    def ct2g(self):
        carat = self.carat * 0.2
        return carat

    def ct2pound(self):
        carat = self.carat * 0.0004
        return carat 

    def ct2quintal(self):
        carat = self.carat * (2 / (10 ** 6))
        return carat

    def ct2milligm(self):
        carat = self.carat * 200
        return carat

    def ct2microgm(self):
        carat = self.carat * 200000
        return carat

    def ct2grain(self):
        carat = self.carat * 3.08
        return carat

    def ct2stone(self):
        carat = self.carat * 3.14
        return carat

    def ct2dram(self):
        carat = self.carat * 0.11
        return carat

# here is the grain Class

class grain:
    grain = 0

    def __init__(self,gr):
        self.grain = gr

    def gr2tonne(self):
        grain = self.grain * (6.479891 / (10 ** 8))
        return grain

    def gr2kg(self):
        grain = self.grain * (6.479891 / (10 ** 5))
        return grain

    def gr2g(self):
        grain = self.grain * 0.064798911
        return grain

    def gr2pound(self):
        grain = self.grain * 0.0001428
        return grain

    def gr2quintal(self):
        grain = self.grain * (6.479891 / (10 ** 7))
        return grain

    def gr2milligm(self):
        grain = self.grain * 64.787
        return grain

    def gr2microgm(self):
        grain = self.grain * 64798
        return grain

    def gr2carat(self):
        grain = self.grain * 0.323
        return grain

    def gr2stone(self):
        grain = self.grain * 1.02
        return grain

    def gr2dram(self):
        grain = self.grain * 0.036
        return grain

# here is the stone Class

class stone:
    stone = 0

    def __init__(self,st):
        self.stone = st

    def st2tonne(self):
        stone = self.stone * 0.0063
        return stone

    def st2kg(self):
        stone = self.stone * 6.35
        return stone

    def st2g(self):
        stone = self.stone * 6350
        return stone

    def st2pound(self):
        stone = self.stone * 14
        return stone

    def st2quintal(self):
        stone = self.stone * 0.063
        return stone

    def st2ounze(self):
        stone = self.stone * 224
        return stone

    def st2milligm(self):
        stone = self.stone * 6350293
        return stone

    def st2microgm(self):
        stone = self.stone * (6.35029318 / (10 ** 9))
        return stone

    def st2carat(self):
        stone = self.stone * 31751
        return stone

    def st2grain(self):
        stone = self.stone * 98000
        return stone

    def st2dram(self):
        stone = self.stone * 3584
        return stone

# here is the dram Class

class dram:
    dram = 0

    def __init__(self,dr):
        self.dram = dr

    def dr2tonne(self):
        dram = self.dram * (1.7718452 / (10 ** 6))
        return dram

    def dr2kg(self):
        dram = self.dram * 0.0017
        return dram

    def dr2g(self):
        dram = self.dram * 1.77
        return dram

    def dr2quintal(self):
        dram = self.dram * (1.7718452 / (10 ** 5))
        return dram

    def dr2pound(self):
        dram = self.dram * 0.0039
        return dram

    def dr2ounze(self):
        dram = self.dram * 0.0625
        return dram

    def dr2milligm(self):
        dram = self.dram * 1771
        return dram

    def dr2microgm(self):
        dram = self.dram * 1771845
        return dram

    def dr2carat(self):
        dram = self.dram * 8.859
        return dram

    def dr2grain(self):
        dram = self.dram * 27
        return dram
    
    def dr2stone(self):
        dram = self.stone * 0.00027
        return dram