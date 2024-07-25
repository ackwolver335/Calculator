# here is another python module containing time convertions units
# the units that would work on this are written as follow
# Year, Weeks, Days, hour, min, sec, millisec, microsec, picosec

class year:
    year = 0

    def __init__(self):
        pass

    def yr2month(self,yr):
        self.year = yr * 12
        return self.year

    def yr2wk(self,yr):
        self.year = yr * 52
        return self.year

    def yr2days(self,yr):
        self.year = yr * 365
        return self.year

    def yr2h(self,yr):
        self.year = yr * 8760
        return self.year

    def yr2min(self,yr):
        self.year = yr * 525600
        return self.year

    def yr2sec(self,yr):
        self.year = yr * 31536000
        return self.year

    def yr2millsec(self,yr):
        self.year = yr * (3.1536 * (10 ** 10))
        return self.year

    def yr2microsec(self,yr):
        self.year = yr * (3.1536 * (10 ** 13))
        return self.year

    def yr2picosec(self,yr):
        self.year = yr * (3.1536 * (10 ** 19))
        return self.year

class week:
    week = 0

    def __init__(self):
        pass

    def wk2yr(self,wk):
        self.week = wk / 52
        return self.week

    def wk2month(self,wk):
        self.week = wk / 4
        return self.week

    def wk2days(self,wk):
        self.week = wk * 7
        return self.week

    def wk2h(self,wk):
        self.week = wk * 168
        return self.week

    def wk2min(self,wk):
        self.week = wk * 10080
        return self.week

    def wk2sec(self,wk):
        self.week = wk * 604800
        return self.week

    def wk2millsec(self,wk):
        self.week = wk * (6048 * (10 ** 5))
        return self.week

    def wk2microsec(self,wk):
        self.week = wk * (6.048 * (10 ** 11))
        return self.week

    def wk2picosec(self,wk):
        self.week = wk * (6.048 * (10 ** 17))
        return self.week

class days:
    days = 0

    def __init__(self):
        pass

    def dy2yr(self,dys):
        self.days = dys / 365
        return self.days

    def dy2month(self,dys):
        self.days = dys / 30
        return self.days

    def dy2wk(self,dys):
        self.days = dys / 7
        return self.days

    def dy2h(self,dys):
        self.days = dys * 24
        return self.days

    def dy2min(self,dys):
        self.days = dys * 1440
        return self.days

    def dy2sec(self,dys):
        self.days = dys * 86400
        return self.days

    def dy2millsec(self,dys):
        self.days = dys * (864 * (10 ** 5))
        return self.days

    def dy2microsec(self,dys):
        self.days = dys * (8.64 * (10 ** 10))
        return self.days

    def dy2picosec(self,dys):
        self.days = dys * (8.64 * (10 ** 16))
        return self.days

class hour:
    hour = 0

    def __init__ (self,h):
        self.hour = h
    
    def h2yr(self):
        hour = self.hour / 8760
        return hour

    def h2month(self):
        hour = self.hour / (24 * 30)
        return hour

    def h2wk(self):
        hour = self.hour / 168
        return hour

    def h2days(self):
        hour = self.hour / 24
        return hour

    def h2min(self):
        hour = self.hour * 60
        return hour

    def h2sec(self):
        hour = self.hour * 3600
        return hour

    def h2millsec(self):
        hour = self.hour * (36 * (10 ** 5))
        return hour

    def h2microsec(self):
        hour = self.hour * (3.6 * (10 ** 9))
        return hour

    def h2picosec(self):
        hour = self.hour * (3.6 * (10 ** 15))
        return hour

class minute:
    minute = 0

    def __init__(self):
        pass

    def min2yr(self,min):
        self.minute = min / 525600
        return self.minute

    def min2month(self,min):
        self.minute = min / (60 * 24 * (30))
        return self.minute

    def min2wk(self,min):
        self.minute = min / 10080
        return self.minute

    def min2days(self,min):
        self.minute = min / 1440
        return self.minute

    def min2h(self,min):
        self.minute = min / 60
        return self.minute

    def min2sec(self,min):
        self.minute = min * 60
        return self.minute 

    def min2millsec(self,min):
        self.minute = min * 60000
        return self.minute

    def min2microsec(self,min):
        self.minute = min * (60 * (10 ** 6))
        return self.minute

    def min2picosec(self,min):
        self.minute = min * (60 * (10 ** 11))
        return self.minute

class second:
    second = 0

    def __init__(self,sec):
        self.second = sec

    def sec2yr(self):
        sec = self.second / 31536000
        return sec

    def sec2wk(self):
        sec = self.second / 604800
        return sec

    def sec2days(self):
        sec = self.second / 86400
        return sec

    def sec2hour(self):
        sec = self.second / 3600
        return sec

    def sec2min(self):
        sec = self.second / 60
        return sec
    
    def sec2millsec(self):
        sec = self.second * 1000
        return sec

    def sec2micorsec(self):
        sec = self.second * (10 ** 6)
        return sec

    def sec2picosec(self):
        sec = self.second * (10 ** 12)
        return sec

class millisec:
    millisec = 0

    def __init__(self,milsec):
        self.millisec = milsec

    def milsec2yr(self):
        millisec = self.millisec / (3.1536 * (10 ** 10))
        return millisec

    def milsec2wk(self):
        millisec = self.millisec / (6048 * (10 ** 5))
        return millisec

    def milsec2days(self):
        millisec = self.millisec / (864 * (10 ** 5))
        return millisec

    def milsec2hr(self):
        millisec = self.millisec / (36 * (10 ** 5))
        return millisec

    def milsec2min(self):
        millisec = self.millisec / 60000
        return millisec

    def milsec2sec(self):
        millisec = self.millisec / 1000
        return millisec

    def milsec2microsec(self):
        millisec = self.millisec * 1000
        return millisec

    def milsec2picosec(self):
        millisec = self.millisec * (10 ** 9)
        return millisec

class microsec:
    microsec = 0

    def __init__(self,mcsec):
        self.microsec = mcsec

    def usec2yr(self):
        microsec = self.microsec / (3.1536 * (10 ** 13))
        return microsec

    def usec2wk(self):
        microsec = self.microsec / (6.048 * (10 ** 11))
        return microsec

    def usec2days(self):
        microsec = self.microsec / (8.64 * (10 ** 10))
        return microsec

    def usec2hr(self):
        microsec = self.microsec / (3.6 * (10 ** 9))
        return microsec

    def usec2min(self):
        microsec = self.microsec / (6 * (10 ** 7))
        return microsec

    def usec2sec(self):
        microsec = self.microsec / (10 ** 6)
        return microsec

    def usec2millisec(self):
        microsec = self.microsec / 1000
        return microsec

    def usec2picosec(self):
        microsec = self.microsec * (10 ** 6)
        return microsec

class picosec:
    picosec = 0

    def __init__(self,pcsec):
        self.picosec = pcsec

    def pcsec2yr(self):
        pcsec = self.picosec / (3.1536 * (10 ** 19))
        return pcsec
    
    def pcsec2wk(self):
        pcsec = self.picosec / (6.048 * (10 ** 17))
        return pcsec

    def pcsec2day(self):
        pcsec = self.picosec / (8.64 * (10 ** 16))
        return pcsec

    def pcsec2hr(self):
        pcsec = self.picosec / (3.6 * (10 ** 15))
        return pcsec

    def pcsec2min(self):
        pcsec = self.picosec / (6 * (10 ** 13))
        return pcsec
    
    def pcsec2sec(self):
        pcsec = self.picosec / (10 ** 12)
        return pcsec

    def pcsec2millisec(self):
        pcsec = self.picosec / (10 ** 9)
        return pcsec

    def pcsec2microsec(self):
        pcsec = self.picosec / (10 ** 6)
        return pcsec