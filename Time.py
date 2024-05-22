# here is another python module containing time convertions units
# the units that would work on this are written as follow
# Year, Weeks, Days, hour, min, sec, millisec, microsec, picosec

class year:
    year = 0

    def __init__(self,yr):
        self.year = yr

    def yr2month(self):
        year = self.year * 12
        return year

    def yr2wk(self):
        year = self.year * 52
        return year

    def yr2days(self):
        year = self.year * 365
        return year

    def yr2h(self):
        year = self.year * 8760
        return year

    def yr2min(self):
        year = self.year * 525600
        return year

    def yr2sec(self):
        year = self.year * 31536000
        return year

    def yr2millsec(self):
        year = self.year * (3.1536 * (10 ** 10))
        return year

    def yr2microsec(self):
        year = self.year * (3.1536 * (10 ** 13))
        return year

    def yr2picosec(self):
        year = self.year * (3.1536 * (10 ** 19))
        return year

class week:
    week = 0

    def __init__(self,wk):
        self.week = wk

    def wk2yr(self):
        week = self.week / 52
        return week

    def wk2month(self):
        week = self.week / 4
        return week

    def wk2days(self):
        week = self.week * 7
        return week

    def wk2h(self):
        week = self.week * 168
        return week

    def wk2min(self):
        week = self.week * 10080
        return week

    def wk2sec(self):
        week = self.week * 604800
        return week

    def wk2millsec(self):
        week = self.week * (6048 * (10 ** 5))
        return week

    def wk2microsec(self):
        week = self.week * (6.048 * (10 ** 11))
        return week

    def wk2picosec(self):
        week = self.week * (6.048 * (10 ** 17))
        return week

class days:
    days = 0

    def __init__(self,dy):
        self.days = dy

    def dy2yr(self):
        days = self.days / 365
        return days

    def dy2month(self):
        days = self.days / 30
        return days

    def dy2wk(self):
        days = self.days / 7
        return days

    def dy2h(self):
        days = self.days * 24
        return days

    def dy2min(self):
        days = self.days * 1440
        return days

    def dy2sec(self):
        days = self.days * 86400
        return days

    def dy2millsec(self):
        days = self.days * (864 * (10 ** 5))
        return days

    def dy2microsec(self):
        days = self.days * (8.64 * (10 ** 10))
        return days

    def dy2picosec(self):
        days = self.days * (8.64 * (10 ** 16))
        return days

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

    def __init(self,min):
        self.minute = min

    def min2yr(self):
        min = self.min / 525600
        return min

    def min2month(self):
        min = self.min / (60 * 24 * (30))
        return min

    def min2wk(self):
        min = self.min / 10080
        return min

    def min2days(self):
        min = self.min / 1440
        return min

    def min2h(self):
        min = self.min / 60

    def min2sec(self):
        min = self.min * 60
        return min 

    def min2millsec(self):
        min = self.min * 60000
        return min

    def min2microsec(self):
        min = self.min * (60 * (10 ** 6))
        return min

    def min2picosec(self):
        min = self.min * (60 * (10 ** 11))
        return min

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