# Here is another data conversion Setup of Memories Specially in Python with it's use
# The units used in it are given below
# Bit, byte, kb, mb, gb, tb, pb, eb, zb, yb

class Bit:
    bit = 0

    def __init__(self,bt):
        self.bit = bt

    def bt2byte(self):
        bit = self.bit / 8
        return bit

    def bt2kb(self):
        bit = self.bit / (8 * 1024)
        return bit

    def bt2mb(self):
        bit = self.bit / (8 * (1024 ** 2))
        return bit

    def bt2gb(self):
        bit = self.bit / (8 * (1024 ** 3))
        return bit

    def bt2tb(self):
        bit = self.bit / (8 * (1024 ** 4))
        return bit

    def bt2pb(self):
        bit = self.bit / (8 * (1024 ** 5))
        return bit

    def bt2eb(self):
        bit = self.bit / (8 * (1024 ** 6))
        return bit

    def bt2zb(self):
        bit = self.bit / (8 * (1024 ** 7))
        return bit

    def bt2yb(self):
        bit = self.bit / (8 * (1024 ** 8))
        return bit

class Byte:
    byte = 0

    def __init__(self,byt):
        self.byte = byt

    def byt2bt(self):
        byte = self.byte * 8
        return byte

    def byt2kb(self):
        byte = self.byte / 1024
        return byte

    def byt2mb(self):
        byte = self.byte / (1024 ** 2)
        return byte
    
    def byt2gb(self):
        byte = self.byte / (1024 ** 3)
        return byte

    def byt2tb(self):
        byte = self.byte / (1024 ** 4)
        return byte
    
    def byt2pb(self):
        byte = self.byte / (1024 ** 5)
        return byte

    def byt2eb(self):
        byte = self.byte / (1024 ** 6)
        return byte

    def byt2zb(self):
        byte = self.byte / (1024 ** 7)
        return byte

    def byt2yb(self):
        byte = self.byte / (1024 ** 8)
        return byte

class kilobyte:
    kilobyt = 0

    def __init__(self,kb):
        self.kilobyt = kb

    def kb2bit(self):
        kilobyt = self.kilobyt * 1024 * 8
        return kilobyt

    def kb2byte(self):
        kilobyt = self.kilobyt * 1024
        return kilobyt

    def kb2mb(self):
        kilobyt = self.kilobyt / 1024
        return kilobyt

    def kb2gb(self):
        kilobyt = self.kilobyt / (1024 ** 2)
        return kilobyt

    def kb2tb(self):
        kilobyt = self.kilobyt / (1024 ** 3)
        return kilobyt

    def kb2pb(self):
        kilobyt = self.kilobyt / (1024 ** 4)
        return kilobyt

    def kb2eb(self):
        kilobyt = self.kilobyt / (1024 ** 5)
        return kilobyt

    def kb2zb(self):
        kilobyt = self.kilobyt / (1024 ** 6)
        return kilobyt
    
    def kb2yb(self):
        kilobyt = self.kilobyt / (1024 ** 7)
        return kilobyt

class megabyte:
    mgbyt = 0

    def __init__(self,mb):
        self.mgbyt = mb
    
    def mb2bit(self):
        mgbyt = self.mgbyt * ((1024 ** 2) * 8)
        return mgbyt

    def mb2byt(self):
        mgbyt = self.mgbyt * (1024 * 8)
        return mgbyt
    
    def mb2kb(self):
        mgbyt = self.mgbyt * 1024
        return mgbyt

    def mb2gb(self):
        mgbyt = self.mgbyt / 1024
        return mgbyt
    
    def mb2tb(self):
        mgbyt = self.mgbyt / (1024 ** 2)
        return mgbyt

    def mb2pb(self):
        mgbyt = self.mgbyt / (1024 ** 3)
        return mgbyt

    def mb2eb(self):
        mgbyt = self.mgbyt / (1024 ** 4)
        return mgbyt

    def mb2zb(self):
        mgbyt = self.mgbyt / (1024 ** 5)
        return mgbyt

    def mb2yb(self):
        mgbyt = self.mgbyt / (1024 ** 6)
        return mgbyt

class gigabyt:
    ggbyt = 0

    def __init__(self,gb):
        self.ggbyt = gb

    def gb2bit(self):
        ggbyt = self.ggbyt * ((1024 ** 3) * 8)
        return ggbyt

    def gb2byte(self):
        ggbyt = self.ggbyt * (1024 ** 3)
        return ggbyt

    def gb2kb(self):
        ggbyt = self.ggbyt * (1024 ** 2)
        return ggbyt

    def gb2mb(self):
        ggbyt = self.ggbyt * 1024
        return ggbyt
    
    def gb2tb(self):
        ggbyt = self.ggbyt / 1024
        return ggbyt

    def gb2pb(self):
        ggbyt = self.ggbyt / (1024 ** 2)
        return ggbyt

    def gb2eb(self):
        ggbyt = self.ggbyt / (1024 ** 3)
        return ggbyt 

    def gb2zb(self):
        ggbyt = self.ggbyt / (1024 ** 4)
        return ggbyt

    def gb2yb(self):
        ggbyt = self.ggbyt / (1024 ** 5)
        return ggbyt

class terabyt:
    tbyt = 0

    def __init__(self,tb):
        self.tbyt = tb

    def tb2bit(self):
        tbyt = self.tbyt * ((1024 ** 4) * 8)
        return tbyt

    def tb2byt(self):
        tbyt = self.tbyt * (1024 ** 4)
        return tbyt

    def tb2kb(self):
        tbyt = self.tbyt * (1024 ** 3)
        return tbyt 

    def tb2mb(self):
        tbyt = self.tbyt * (1024 ** 2)
        return tbyt

    def tb2gb(self):
        tbyt = self.tbyt * 1024
        return tbyt

    def tb2pb(self):
        tbyt = self.tbyt / 1024
        return tbyt

    def tb2eb(self):
        tbyt = self.tbyt / (1024 ** 2)
        return tbyt

    def tb2zb(self):
        tbyt = self.tbyt / (1024 ** 3)
        return tbyt

    def tb2yb(self):
        tbyt = self.tbyt / (1024 ** 4)
        return tbyt

class picobyt:
    pcbyt = 0

    def __init__(self,pb):
        self.pcbyt = pb

    def pb2bit(self):
        pcbyt = self.pcbyt * ((1024 ** 5) * 8)
        return pcbyt

    def pb2byt(self):
        pcbyt = self.pcbyt * (1024 ** 5)
        return pcbyt

    def pb2kb(self):
        pcbyt = self.pcbyt * (1024 ** 4)
        return pcbyt

    def pb2mb(self):
        pcbyt = self.pcbyt * (1024 ** 3)
        return pcbyt

    def pb2gb(self):
        pcbyt = self.pcbyt * (1024 ** 2)
        return pcbyt

    def pb2tb(self):
        pcbyt = self.pcbyt * 1024
        return pcbyt
    
    def pb2eb(self):
        pcbyt = self.pcbyt / 1024
        return pcbyt

    def pb2zb(self):
        pcbyt = self.pcbyt / (1024 ** 2)
        return pcbyt

    def pb2yb(self):
        pcbyt = self.pcbyt / (1024 ** 3)
        return pcbyt

class exabyt:
    exbyt = 0

    def __init__(self,eb):
        self.exbyt = eb
    
    def eb2bit(self):
        exbyt = self.exbyt * ((1024 ** 6) * 8)
        return exbyt

    def eb2byt(self):
        exbyt = self.exbyt * (1024 ** 6)
        return exbyt

    def eb2kb(self):
        exbyt = self.exbyt * (1024 ** 5)
        return exbyt

    def eb2mb(self):
        exbyt = self.exbyt * (1024 ** 4)
        return exbyt 

    def eb2gb(self):
        exbyt = self.exbyt * (1024 ** 3)
        return exbyt

    def eb2tb(self):
        exbyt = self.exbyt * (1024 ** 2)
        return exbyt

    def eb2pb(self):
        exbyt = self.exbyt * 1024
        return exbyt
    
    def eb2zb(self):
        exbyt = self.exbyt / 1024
        return exbyt

    def eb2yb(self):
        exbyt = self.exbyt / (1024 ** 2)
        return exbyt

class zetabyte:
    ztbyt = 0

    def __init__(self,zb):
        self.ztbyt = zb

    def zb2bit(self):
        ztbyt = self.ztbyt * ((1024 ** 7) * 8)
        return ztbyt

    def zb2byt(self):
        ztbyt = self.ztbyt * (1024 ** 7)
        return ztbyt
    
    def zb2kb(self):
        ztbyt = self.ztbyt * (1024 ** 6)
        return ztbyt

    def zb2mb(self):
        ztbyt = self.ztbyt * (1024 ** 5)
        return ztbyt
    
    def zb2gb(self):
        ztbyt = self.ztbyt * (1024 ** 4)
        return ztbyt 

    def zb2tb(self):
        ztbyt = self.ztbyt * (1024 ** 3)
        return ztbyt
    
    def zb2pb(self):
        ztbyt = self.ztbyt * (1024 ** 2)
        return ztbyt
    
    def zb2eb(self):
        ztbyt = self.ztbyt * 1024
        return ztbyt

    def zb2yb(self):
        ztbyt = self.ztbyt / 1024
        return ztbyt

class yotabyte:
    ytbty = 0

    def __init__(self,yb):
        self.ytbyt = yb
    
    def yb2bit(self):
        ytbyt = self.ytbyt * ((1024 ** 8) * 8)
        return ytbyt

    def yb2byt(self):
        ytbyt = self.ytbyt * (1024 ** 8)
        return ytbyt
    
    def yb2kb(self):
        ytbyt = self.ytbyt * (1024 ** 7)
        return ytbyt
    
    def yb2mb(self):
        ytbyt = self.ytbyt * (1024 ** 6)
        return ytbyt

    def yb2gb(self):
        ytbyt = self.ytbyt * (1024 ** 5)
        return ytbyt

    def yb2tb(self):
        ytbyt = self.ytbyt * (1024 ** 4)
        return ytbyt 

    def yb2pb(self):
        ytbyt = self.ytbyt * (1024 ** 3)
        return ytbyt

    def yb2eb(self):
        ytbyt = self.ytbyt * (1024 ** 2)
        return ytbyt 

    def yb2zb(self):
        ytbyt = self.ytbyt * 1024
        return ytbyt