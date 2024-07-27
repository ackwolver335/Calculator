# Here is another Library of Python which contains the conversion of Volume's units
# The units used in this one are as follow
# mtr3, dm3, cm3, mm3, hl, ltr, dcltr, cntltr, mlltr, ft3, inch3, yd3, af3

class metre3:
    meter_cub = 0

    def __init__(self):
        pass

    def mcub2dmcub(self,m3):
        self.meter_cub = m3 * 1000
        return self.meter_cub

    def mcub2cmcub(self,m3):
        self.meter_cub = m3 * (10 ** 6)
        return self.meter_cub

    def mcub2mmcub(self,m3):
        self.meter_cub = m3 * (10 ** 9)
        return self.meter_cub

    def mcub2hctl(self,m3):
        self.meter_cub = m3 * 10
        return self.meter_cub

    def mcub2ltr(self,m3):
        self.meter_cub = m3 * 1000
        return self.meter_cub

    def mcub2dcltr(self,m3):
        self.meter_cub = m3 * (10 ** 4)
        return self.meter_cub

    def mcub2mltr(self,m3):
        self.meter_cub = m3 * (10 ** 6)
        return self.meter_cub

    def mcub2ft3(self,m3):
        self.meter_cub = m3 * 35
        return self.meter_cub

    def mcub2inch3(self,m3):
        self.meter_cub = m3 * 61023
        return self.meter_cub

    def mcub2yd3(self,m3):
        self.meter_cub = m3 * 1.307
        return self.meter_cub

    def mcub2af3(self,m3):
        self.meter_cub = m3 / 1234
        return self.meter_cub

class decimtr3:
    decimtr3 = 0

    def __init__(self,dcm3):
        pass

    def decimcub2mtr3(self,dcm3):
        self.decimtr3 = dcm3 / 1000
        return self.decimtr3

    def decimcub2cm3(self,dcm3):
        self.decimtr3 = dcm3 * 1000
        return self.decimtr3

    def decimcub2mm3(self,dcm3):
        self.decimtr3 = dcm3 * (10 ** 6)
        return self.decimtr3

    def decimcub2hl(self,dcm3):
        self.decimtr3 = dcm3 / 100
        return self.decimtr3

    def decimcub2l(self,dcm3):
        self.decimtr3 = dcm3 * 1
        return self.decimtr3

    def decimcub2dl(self,dcm3):
        self.decimtr3 = dcm3 * 10
        return self.decimtr3

    def decimcub2cl(self,dcm3):
        self.decimtr3 = dcm3 * 100
        return self.decimtr3

    def decimcub2ml(self,dcm3):
        self.decimtr3 = dcm3 * 1000
        return self.decimtr3

    def decimcub2ft3(self,dcm3):
        self.decimtr3 = dcm3 / 28
        return self.decimtr3

    def decimcub2inch3(self,dcm3):
        self.decimtr3 = dcm3 * 61
        return self.decimtr3

    def decimcub2yd3(self,dcm3):
        self.decimtr3 = dcm3 / 764
        return self.decimtr3

    def decimcub2af3(self,dcm3):
        self.decimtr3 = dcm3 / 1234000
        return self.decimtr3

class centimtr3:
    centimtr3 = 0

    def __init__(self,cm3):
        self.centimtr3 = cm3

    def cmcub2m3(self):
        centimtr3 = self.centimtr3 / (10 ** 6)
        return centimtr3

    def cmcub2dm3(self):
        centimtr3 = self.centimtr3 / 1000
        return centimtr3

    def cmcub2mm3(self):
        centimtr3 = self.centimtr3 * 1000
        return centimtr3

    def cmcub2hl(self):
        centimtr3 = self.centimtr3 / (10 ** 5)
        return centimtr3

    def cmcub2l(self):
        centimtr3 = self.centimtr3 / 1000
        return centimtr3

    def cmcub2dl(self):
        centimtr3 = self.centimtr3 / 100
        return centimtr3

    def cmcub2cl(self):
        centimtr3 = self.centimtr3 / 10
        return centimtr3

    def cmcub2ml(self):
        centimtr3 = self.centimtr3 * 1
        return centimtr3

    def cmcub2ft3(self):
        centimtr3 = self.centimtr3 / 28316
        return centimtr3

    def cmcub2inch3(self):
        centimtr3 = self.centimtr3 / 16
        return centimtr3

    def cmcub2yd3(self):
        centimtr3 = self.centimtr3 / 764554
        return centimtr3

    def cmcub2af3(self):
        centimtr3 = self.centimtr3 / (1.234 * (10 ** 9))
        return centimtr3

class millimtr3:
    millimtr3 = 0

    def __init__(self,mm):
        self.millimtr3 = mm

    def mmcub2m3(self):
        millimtr3 = self.millimtr3 / (10 ** 9)
        return millimtr3
    
    def mmcub2dm3(self):
        millimtr3 = self.millimtr3 / (10 ** 6)
        return millimtr3

    def mmcub2cm3(self):
        millimtr3 = self.millimtr3 / 1000
        return millimtr3
        
    def mmcub2hl(self):
        millimtr3 = self.millimtr3 / (10 ** 8)
        return millimtr3

    def mmcub2l(self):
        millimtr3 = self.millimtr3 / (10 ** 6)
        return millimtr3

    def mmcub2dl(self):
        millimtr3 = self.millimtr3 / (10 ** 5)
        return millimtr3

    def mmcub2cl(self):
        millimtr3 = self.millimtr3 / (10 ** 4)
        return millimtr3

    def mmcub2ml(self):
        millimtr3 = self.millimtr3 / 1000
        return millimtr3

    def mmcub2ft3(self):
        millimtr3 = self.millimtr3 / 28316846
        return millimtr3

    def mmcub2inch3(self):
        millimtr3 = self.millimtr3 / 16387
        return millimtr3

    def mmcub2yd3(self):
        millimtr3 = self.millimtr3 / 764554858
        return millimtr3

    def mmcub2af3(self):
        millimtr3 = self.millimtr3 / (1234 * (10 ** 12))
        return millimtr3

class hectltr:
    hectltr = 0

    def __init__(self,hltr):
        self.hectltr = hltr

    def hltr2m3(self):
        hectltr = self.hectltr / 10
        return hectltr

    def hltr2dm3(self):
        hectltr = self.hectltr * 100
        return hectltr
    
    def hltr2cm3(self):
        hectltr = self.hectltr * (10 ** 5)
        return hectltr

    def hltr2mm3(self):
        hectltr = self.hectltr * (10 ** 8)
        return hectltr

    def hltr2l(self):
        hectltr = self.hectltr * 100
        return hectltr

    def hltr2dl(self):
        hectltr = self.hectltr * 1000
        return hectltr

    def hltr2cl(self):
        hectltr = self.hectltr * (10 ** 4)
        return hectltr 

    def hltr2ml(self):
        hectltr = self.hectltr * (10 ** 5)
        return hectltr

    def hltr2ft3(self):
        hectltr = self.hectltr * 3.5
        return hectltr

    def hltr2inch3(self):
        hectltr = self.hectltr * 6102
        return hectltr

    def hltr2yd3(self):
        hectltr = self.hectltr / 7
        return hectltr

    def hltr2af3(self):
        hectltr = self.hectltr / 12340
        return hectltr

class ltr:
    litre = 0

    def __init__(self,ltr):
        self.litre = ltr

    def ltr2m3(self):
        litre = self.litre / 1000
        return litre

    def ltr2dm3(self):
        litre = self.litre * 1
        return litre

    def ltr2cm3(self):
        litre = self.litre * 1000
        return litre

    def ltr2mm3(self):
        litre = self.litre * (10 ** 6)
        return litre

    def ltr2hl(self):
        litre = self.litre / 100
        return litre

    def ltr2dl(self):
        litre = self.litre * 10
        return litre

    def ltr2cl(self):
        litre = self.litre * 100
        return litre

    def ltr2ml(self):
        litre = self.litre * 1000
        return litre

    def ltr2ft3(self):
        litre = self.litre / 28
        return litre

    def ltr2inch3(self):
        litre = self.litre * 61
        return litre

    def ltr2yd3(self):
        litre = self.litre * 764
        return litre

    def ltr2af3(self):
        litre = self.litre / 1234000
        return litre

class decilitre:
    decltr = 0

    def __init__(self,dl):
        self.decltr = dl

    def decl2m3(self):
        decltr = self.decltr / 10000
        return decltr

    def decl2dm3(self):
        decltr = self.decltr / 10
        return decltr

    def decl2cm3(self):
        decltr = self.decltr * 100
        return decltr

    def decl2mm3(self):
        decltr = self.decltr * (10 ** 5)
        return decltr

    def decl2hl(self):
        decltr = self.decltr / 1000
        return decltr

    def decl2l(self):
        decltr = self.decltr / 10
        return decltr

    def decl2cl(self):
        decltr = self.decltr * 10
        return decltr
    
    def decl2ml(self):
        decltr = self.decltr * 100
        return decltr

    def decl2ft3(self):
        decltr = self.decltr / 283
        return decltr
    
    def decl2inch3(self):
        decltr = self.decltr * 6
        return decltr

    def decl2yd3(self):
        decltr = self.decltr / 7645
        return decltr

    def decl2af3(self):
        decltr = self.decltr / (1234 * (10 ** 4))
        return decltr

class centiltr:
    cntlt = 0

    def __init__(self,ctlt):
        self.cntlt = ctlt
    
    def cntlt2m3(self):
        cntlt = self.cntlt / (10 ** 5)
        return cntlt

    def cntlt2dm3(self):
        cntlt = self.cntlt / 100
        return cntlt

    def cntlt2cm3(self):
        cntlt = self.cntlt * 10
        return cntlt

    def cntlt2mm3(self):
        cntlt = self.cntlt * (10 ** 4)
        return cntlt

    def cntlt2hl(self):
        cntlt = self.cntlt / (10 ** 4)
        return cntlt

    def cntlt2l(self):
        cntlt = self.cntlt / 100
        return cntlt

    def cntlt2dl(self):
        cntlt = self.cntlt / 10
        return cntlt

    def cntlt2ml(self):
        cntlt = self.cntlt * 10
        return cntlt
    
    def cntlt2ft3(self):
        cntlt = self.cntlt / 2831
        return cntlt
    
    def cntlt2inch3(self):
        cntlt = self.cntlt / 1.6
        return cntlt
    
    def cntlt2yd3(self):
        cntlt = self.cntlt / 76455
        return cntlt

    def cntlt2af3(self):
        cntlt = self.cntlt / (1234 * (10 ** 4))
        return cntlt

class milliltr:
    mlltr = 0

    def __init__(self,milliltr):
        self.mlltr = milliltr

    def ml2m3(self):
        mlltr = self.mlltr / (10 ** 6)
        return mlltr
    
    def ml2dm3(self):
        mlltr = self.mlltr / 1000
        return mlltr

    def ml2cm3(self):
        mlltr = self.mlltr * 1
        return mlltr

    def ml2mm3(self):
        mlltr = self.mlltr * 1000
        return mlltr

    def ml2hl(self):
        mlltr = self.mlltr / (10 ** 5)
        return mlltr

    def ml2l(self):
        mlltr = self.mlltr / 1000
        return mlltr

    def ml2cl(self):
        mlltr = self.mlltr / 10
        return mlltr

    def ml2dl(self):
        mlltr = self.mlltr / 100
        return mlltr

    def ml2ft3(self):
        mlltr = self.mlltr / 28316
        return mlltr

    def ml2inch3(self):
        mlltr = self.mlltr / 16
        return mlltr
    
    def ml2yd3(self):
        mlltr = self.mlltr / 765554
        return mlltr

    def ml2af3(self):
        mlltr = self.mlltr / (1234 * (10 ** 9))
        return mlltr
    
class footcub:
    ftcub = 0

    def __init__(self,ft3):
        self.ftcub = ft3

    def ftcub2m3(self):
        ftcub = self.ftcub / 35
        return ftcub

    def ftcub2dm3(self):
        ftcub = self.ftcub * 28
        return ftcub

    def ftcub2cm3(self):
        ftcub = self.ftcub * 28316
        return ftcub

    def ftcub2mm3(self):
        ftcub = self.ftcub * 28316846
        return ftcub
    
    def ftcub2hl(self):
        ftcub = self.ftcub / 3.5
        return ftcub

    def ftcub2l(self):
        ftcub = self.ftcub * 28
        return ftcub

    def ftcub2dl(self):
        ftcub = self.ftcub * 283
        return ftcub

    def ftcub2cl(self):
        ftcub = self.ftcub * 2831
        return ftcub
    
    def ftcub2ml(self):
        ftcub = self.ftcub * 28316
        return ftcub
    
    def ftcub2inch3(self):
        ftcub = self.ftcub * 1728
        return ftcub

    def ftcub2yd3(self):
        ftcub = self.ftcub / 27
        return ftcub

    def ftcub2af3(self):
        ftcub = self.ftcub / 43578
        return ftcub
    
class inchcub:
    ihcub = 0

    def __init__(self,inch3):
        self.ihcub = inch3

    def ihcub2m3(self):
        ihcub = self.ihcub / 61023
        return ihcub

    def ihcub2dm3(self):
        ihcub = self.ihcub / 61
        return ihcub

    def ihcub2cm3(self):
        ihcub = self.ihcub * 16
        return ihcub

    def ihcub2mm3(self):
        ihcub = self.ihcub * 16387
        return ihcub

    def ihcub2hl(self):
        ihcub = self.ihcub / 6102
        return ihcub

    def ihcub2l(self):
        ihcub = self.ihcub / 61
        return ihcub

    def ihcub2dl(self):
        ihcub = self.ihcub / 6
        return ihcub

    def ihcub2cl(self):
        ihcub = self.ihcub * 1.63
        return ihcub

    def ihcub2ml(self):
        ihcub = self.ihcub * 16
        return ihcub

    def ihcub2ft3(self):
        ihcub = self.ihcub / 1728
        return ihcub

    def ihcub2yd3(self):
        ihcub = self.ihcub / 46656
        return ihcub

    def ihcub2af3(self):
        ihcub = self.ihcub / 75303300
        return ihcub

class yardcub:
    ydcub = 0
    
    def __init(self,yd3):
        self.ydcub = yd3

    def ydcub2m3(self):
        ydcub = self.ydcub / 1.3
        return ydcub

    def ydcub2dm3(self):
        ydcub = self.ydcub * 764
        return ydcub

    def ydcub2cm3(self):
        ydcub = self.ydcub * 764554
        return ydcub

    def ydcub2mm3(self):
        ydcub = self.ydcub * 764554858
        return ydcub

    def ydcub2hl(self):
        ydcub = self.ydcub * 7.6
        return ydcub

    def ydcub2l(self):
        ydcub = self.ydcub * 764
        return ydcub

    def ydcub2dl(self):
        ydcub = self.ydcub * 7645
        return ydcub

    def ydcub2cl(self):
        ydcub = self.ydcub * 76455
        return ydcub

    def ydcub2ml(self):
        ydcub = self.ydcub * 764554
        return ydcub

    def ydcub2ft3(self):
        ydcub = self.ydcub * 27
        return ydcub

    def ydcub2inch3(self):
        ydcub = self.ydcub * 46656
        return ydcub

    def ydcub2af3(self):
        ydcub = self.ydcub / 1614
        return ydcub

class areafoot3:
    aftcub = 0

    def __init__(self,af3):
        self.aftcub = af3

    def aftcub2m3(self):
        aftcub = self.aftcub * 1234
        return aftcub

    def aftcub2dm3(self):
        aftcub = self.aftcub * 1234000
        return aftcub

    def aftcub2cm3(self):
        aftcub = self.aftcub * (1.234 * (10 ** 9))
        return aftcub

    def aftcub2mm3(self):
        aftcub = self.aftcub * (1.234 * (10 ** 12))
        return aftcub

    def aftcub2hl(self):
        aftcub = self.aftcub * 12340
        return aftcub

    def aftcub2l(self):
        aftcub = self.aftcub * 1234000
        return aftcub

    def aftcub2dl(self):
        aftcub = self.aftcub * (1234 * (10 ** 4))
        return aftcub

    def aftcub2cl(self):
        aftcub = self.aftcub * (1234 * (10 ** 5))
        return aftcub

    def aftcub2ml(self):
        aftcub = self.aftcub * (1.234 * (10 ** 9))
        return aftcub

    def aftcub2ft3(self):
        aftcub = self.aftcub * 43578
        return aftcub

    def aftcub2inch3(self):
        aftcub = self.aftcub * 75303300
        return aftcub

    def aftcub2yd3(self):
        aftcub = self.aftcub * 1614
        return aftcub