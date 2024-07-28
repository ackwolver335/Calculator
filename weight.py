# Here is the Program which contain the function of weight converting in it differently
# This Module contains the functions in classes of these weights units
# kg, g, tonne, milligm, microgm, pound, quintal, ounze, carat, grain, stone, dram

# Let us start making the functions
# Here I have created a class for all kilogram conversion functions

# here is the KG Class

class kilogram:
    kilogram = None

    def __init__(self):
        pass

    def kg2g(self,kg):                        
        self.kilogram = kg * 1000
        return self.kilogram

    def kg2milligm(self,kg):                  
        self.kilogram = kg * (10 ** 6)
        return self.kilogram

    def kg2microgm(self,kg):                  
        self.kilogram = kg * (10 ** 9)
        return self.kilogram

    def kg2tonne(self,kg):                    
        self.kilogram = kg / 1000
        return self.kilogram

    def kg2quintal(self,kg):                  
        self.kilogram = kg / 100
        return self.kilogram

    def kg2pound(self,kg):                    
        self.kilogram = kg * 2.2
        return self.kilogram

    def kg2ounce(self,kg):                    
        self.kilogram = kg * 35.2
        return self.kilogram

    def kg2carat(self,kg):                    
        self.kilogram = kg * 5000
        return self.kilogram

    def kg2grain(self,kg):                    
        self.kilogram = kg * 15432
        return self.kilogram

    def kg2st(self,kg):                       
        self.kilogram = kg * 0.15
        return self.kilogram

    def kg2dr(self,kg):                       
        self.kilogram = kg * 564
        return self.kilogram

# Here I have created a gram class similar to that of kilogram'e one

class gram:
    gram = 0

    def __init__(self):
        pass

    def g2tonne(self,grm):                      
        self.gram = grm / (10 ** 6)
        return self.gram

    def g2kg(self,grm):                         
        self.gram = grm / 1000
        return self.gram

    def g2mg(self,grm):                         
        self.gram = grm * 1000
        return self.gram

    def g2microg(self,grm):                     
        self.gram = grm * (10 ** 6)
        return self.gram

    def g2quintal(self,grm):                    
        self.gram = grm / (10 ** 5)
        return self.gram

    def g2pound(self,grm):                      
        self.gram = grm * 0.0022
        return self.gram

    def g2ounce(self,grm):                      
        self.gram = grm * 0.035
        return self.gram

    def g2carat(self,grm):                      
        self.gram = grm * 5
        return self.gram

    def g2grain(self,grm):                      
        self.gram = grm * 15.4
        return self.gram

    def g2stone(self,grm):                      
        self.gram = grm * 0.00015
        return self.gram

    def g2dram(self,grm):                       
        self.gram = grm * 0.5643
        return self.gram

# Here are the tonne conversion functions containing classes

class tonne:
    tonne = 0

    def __init__(self):
        pass

    def tonne2kg(self,tn):
        self.tonne = tn * 1000
        return self.tonne

    def tonne2g(self,tn):
        self.tonne  = tn * (10 ** 6)
        return self.tonne

    def tonne2milligm(self,tn):
        self.tonne = tn * (10 ** 9)
        return self.tonne

    def tonne2microgm(self,tn):
        self.tonne = tn * (10 ** 12)
        return self.tonne

    def tonne2quintal(self,tn):
        self.tonne = tn * 10
        return self.tonne

    def tonne2pound(self,tn):
        self.tonne = tn * 2.204
        return self.tonne

    def tonne2ounce(self,tn):
        self.tonne = tn * 35273
        return self.tonne

    def tonne_to_carat(self,tn):
        self.tonne = tn * (5 * (10 ** 6))
        return self.tonne

    def tonne2grain(self,tn):
        self.tonne = tn * 15432358
        return self.tonne

    def tonne2stone(self,tn):
        self.tonne = tn * 160
        return self.tonne

    def tonne2dram(self,tn):
        self.tonne = tn * 573440
        return self.tonne

# Here are the milligm conversion classes

class milligm:
    milligm = 0

    def __init__(self):
        pass

    def milligm2tonne(self,mllgm):
        self.milligm = mllgm / (10 ** 9)
        return self.milligm

    def milligm2kg(self,mllgm):
        self.milligm = mllgm / (10 ** 6)
        return self.milligm

    def milligm2g(self,mllgm):
        self.milligm = mllgm / 1000
        return self.milligm

    def milligm2micro(self,mllgm):
        self.milligm = mllgm * 1000
        return self.milligm

    def milligm2quintal(self,mllgm):
        self.milligm = mllgm / (10 ** 8)
        return self.milligm

    def milligm2pound(self,mllgm):
        self.milligm = mllgm * 2.204622
        return self.milligm

    def milligm2ounze(self,mllgm):
        self.milligm = mllgm * 3.527396
        return self.milligm

    def milligm2carat(self,mllgm):
        self.milligm = mllgm * 0.005
        return self.milligm

    def milligm2grain(self,mllgm):
        self.milligm = mllgm * 0.0154323
        return self.milligm

    def milligm2stone(self,mllgm):
        self.milligm = mllgm * 1.57473044
        return self.milligm

    def milligm2dram(self,mllgm):
        self.milligm = mllgm * 0.000564383
        return self.milligm

# here is another class of microgram

class microgram:
    microgm = 0

    def __init__(self):
        pass

    def microgm2tonne(self,mcrgm):
        self.microgm = mcrgm / (10 ** 12)
        return self.microgm

    def microgm2kg(self,mcrgm):
        self.microgm = mcrgm / (10 ** 9)
        return self.microgm

    def microgm2g(self,mcrgm):
        self.microgm = mcrgm / (10 ** 6)
        return self.microgm

    def microgm2milligm(self,mcrgm):
        self.microgm = mcrgm * 1000
        return self.microgm

    def microgm2quintal(self,mcrgm):
        self.microgm = mcrgm / (10 ** 11)
        return self.microgm

    def microgm2pound(self,mcrgm):
        self.microgm = mcrgm * 2.20462262
        return self.microgm

    def microgm2ounze(self,mcrgm):
        self.microgm = mcrgm * 3.52739619
        return self.microgm

    def microgm2carat(self,mcrgm):
        self.microgm = mcrgm / (5 * (10 ** 6))
        return self.microgm

    def microgm2grain(self,mcrgm):
        self.microgm = mcrgm * 1.54323584
        return self.microgm

    def microgm2stone(self,mcrgm):
        self.microgm = mcrgm * (1.57473044 / (10 ** 10))
        return self.microgm

    def microgm2dram(self,mcrgm):
        self.microgm = mcrgm * (5.64383391 / (10 ** 7))
        return self.microgm

# here is the Pound Class

class pound:
    pound = 0

    def __init__(self):
        pass

    def pd2kg(self,pnd):
        self.pound = pnd * 0.453
        return self.pound

    def pd2g(self,pnd):
        self.pound = pnd * 453
        return self.pound

    def pd2tonne(self,pnd):
        self.pound = pnd * (453 / (10 ** 5))
        return self.pound

    def pd2milligm(self,pnd):
        self.pound = pnd * 453592
        return self.pound

    def pd2microgm(self,pnd):
        self.pound = pnd * 453592370
        return self.pound

    def pd2quintal(self,pnd):
        self.pound = pnd * (453 / (10 ** 3))
        return self.pound

    def pd2ounze(self,pnd):
        self.pound = pnd * 16
        return self.pound

    def pd2carat(self,pnd):
        self.pound = pnd * 2267
        return self.pound

    def pd2grain(self,pnd):
        self.pound = pnd * 7000
        return self.pound

    def pd2stone(self,pnd):
        self.pound = pnd * (714 / (10 ** 2))
        return self.pound

    def pd2dram(self,pnd):
        self.pound = pnd * 256
        return self.pound

# here is the Quintal Class

class quintal:
    quintal = 0

    def __init__(self):
        pass

    def qn2tonne(self,qntl):
        self.quintal = qntl * 0.1
        return self.quintal

    def qn2kg(self,qntl):
        self.quintal = qntl * 100
        return self.quintal

    def qn2g(self,qntl):
        self.quintal = qntl * (10 ** 5)
        return self.quintal

    def qn2pound(self,qntl):
        self.quintal = qntl * 220.46
        return self.quintal

    def qn2milligm(self,qntl):
        self.quintal = qntl * (10 ** 8)
        return self.quintal

    def qn2microgm(self,qntl):
        self.quintal = qntl * (10 ** 11)
        return self.quintal

    def qn2ounze(self,qntl):
        self.quintal = qntl * 3527
        return self.quintal

    def qn2carat(self,qntl):
        self.quintal = qntl * (5 * (10 ** 5))
        return self.quintal

    def qn2grain(self,qntl):
        self.quintal = qntl * 1543235
        return self.quintal

    def qn2stone(self,qntl):
        self.quintal = qntl * 15.74
        return self.quintal

    def qn2dram(self,qntl):
        self.quintal = qntl * 56438
        return self.quintal

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
        dram = self.dram * 0.00027
        return dram