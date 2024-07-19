# Here is another data conversion Setup of Memories Specially in Python with it's use
# The units used in it are given below
# Bit, byte, kb, mb, gb, tb, pb, eb, zb, yb

class Bit:
    bit = 0

    def __init__(self):
        pass

    def bt2byte(self,bt):
        self.bit = bit / 8
        return self.bit

    def bt2kb(self,bt):
        self.bit = bit / (8 * 1024)
        return self.bit

    def bt2mb(self,bt):
        self.bit = bt / (8 * (1024 ** 2))
        return self.bit

    def bt2gb(self,bt):
        self.bit = bt / (8 * (1024 ** 3))
        return self.bit

    def bt2tb(self,bt):
        self.bit = bt / (8 * (1024 ** 4))
        return self.bit

    def bt2pb(self,bt):
        self.bit = bt / (8 * (1024 ** 5))
        return self.bit

    def bt2eb(self,bt):
        self.bit = bt / (8 * (1024 ** 6))
        return self.bit

    def bt2zb(self,bt):
        self.bit = bt / (8 * (1024 ** 7))
        return self.bit

    def bt2yb(self,bt):
        self.bit = bt / (8 * (1024 ** 8))
        return self.bit

class Byte:
    byte = 0

    def __init__(self):
        pass

    def byt2bt(self,byt):
        self.byte = byt * 8
        return self.byte

    def byt2kb(self,byt):
        self.byte = byt / 1024
        return self.byte

    def byt2mb(self,byt):
        self.byte = byt / (1024 ** 2)
        return self.byte
    
    def byt2gb(self,byt):
        self.byte = byt / (1024 ** 3)
        return self.byte

    def byt2tb(self,byt):
        self.byte = byt / (1024 ** 4)
        return self.byte
    
    def byt2pb(self,byt):
        self.byte = byt / (1024 ** 5)
        return self.byte

    def byt2eb(self,byt):
        self.byte = byt / (1024 ** 6)
        return self.byte

    def byt2zb(self,byt):
        self.byte = byt / (1024 ** 7)
        return self.byte

    def byt2yb(self,byt):
        self.byte = byt / (1024 ** 8)
        return self.byte

class kilobyte:
    kilobyt = 0

    def __init__(self):
        pass

    def kb2bit(self,kb):
        self.kilobyt = kb * 1024 * 8
        return self.kilobyt

    def kb2byte(self,kb):
        self.kilobyt = self.kilobyt * 1024
        return self.kilobyt

    def kb2mb(self,kb):
        self.kilobyt = kb / 1024
        return self.kilobyt

    def kb2gb(self,kb):
        self.kilobyt = kb / (1024 ** 2)
        return self.kilobyt

    def kb2tb(self,kb):
        self.kilobyt = kb / (1024 ** 3)
        return self.kilobyt

    def kb2pb(self,kb):
        self.kilobyt = kb / (1024 ** 4)
        return self.kilobyt

    def kb2eb(self,kb):
        self.kilobyt = kb / (1024 ** 5)
        return self.kilobyt

    def kb2zb(self,kb):
        self.kilobyt = kb / (1024 ** 6)
        return self.kilobyt
    
    def kb2yb(self,kb):
        self.kilobyt = kb / (1024 ** 7)
        return self.kilobyt

class megabyte:
    mgbyt = 0

    def __init__(self):
        pass
    
    def mb2bit(self,kb):
        self.mgbyt = mb * ((1024 ** 2) * 8)
        return self.mgbyt

    def mb2byt(self,kb):
        self.mgbyt = mb * (1024 * 8)
        return self.mgbyt
    
    def mb2kb(self,kb):
        self.mgbyt = mb * 1024
        return self.mgbyt

    def mb2gb(self,kb):
        self.mgbyt = mb / 1024
        return self.mgbyt
    
    def mb2tb(self,kb):
        self.mgbyt = mb / (1024 ** 2)
        return self.mgbyt

    def mb2pb(self,kb):
        self.mgbyt = mb / (1024 ** 3)
        return self.mgbyt

    def mb2eb(self,kb):
        self.mgbyt = mb / (1024 ** 4)
        return self.mgbyt

    def mb2zb(self,kb):
        self.mgbyt = mb / (1024 ** 5)
        return self.mgbyt

    def mb2yb(self,kb):
        self.mgbyt = mb / (1024 ** 6)
        return self.mgbyt

class gigabyt:
    ggbyt = 0

    def __init__(self):
        pass

    def gb2bit(self,gb):
        self.ggbyt = gb * ((1024 ** 3) * 8)
        return self.ggbyt

    def gb2byte(self,gb):
        self.ggbyt = gb * (1024 ** 3)
        return self.ggbyt

    def gb2kb(self,gb):
        self.ggbyt = gb * (1024 ** 2)
        return self.ggbyt

    def gb2mb(self,gb):
        self.ggbyt = gb * 1024
        return self.ggbyt
    
    def gb2tb(self,gb):
        self.ggbyt = gb / 1024
        return self.ggbyt

    def gb2pb(self,gb):
        self.ggbyt = gb / (1024 ** 2)
        return self.ggbyt

    def gb2eb(self,gb):
        self.ggbyt = gb / (1024 ** 3)
        return self.ggbyt 

    def gb2zb(self,gb):
        self.ggbyt = gb / (1024 ** 4)
        return self.ggbyt

    def gb2yb(self,gb):
        self.ggbyt = gb / (1024 ** 5)
        return self.ggbyt

class terabyt:
    tbyt = 0

    def __init__(self):
        pass

    def tb2bit(self,tb):
        self.tbyt = tb * ((1024 ** 4) * 8)
        return self.tbyt

    def tb2byt(self,tb):
        self.tbyt = tb * (1024 ** 4)
        return self.tbyt

    def tb2kb(self,tb):
        self.tbyt = tb * (1024 ** 3)
        return self.tbyt 

    def tb2mb(self,tb):
        self.tbyt = tb * (1024 ** 2)
        return self.tbyt

    def tb2gb(self,tb):
        self.tbyt = tb * 1024
        return self.tbyt

    def tb2pb(self,tb):
        self.tbyt = tb / 1024
        return self.tbyt

    def tb2eb(self,tb):
        self.tbyt = tb / (1024 ** 2)
        return self.tbyt

    def tb2zb(self,tb):
        self.tbyt = tb / (1024 ** 3)
        return self.tbyt

    def tb2yb(self,tb):
        self.tbyt = tb / (1024 ** 4)
        return self.tbyt

class picobyt:
    pcbyt = 0

    def __init__(self):
        pass

    def pb2bit(self,pb):
        self.pcbyt = pb * ((1024 ** 5) * 8)
        return self.pcbyt

    def pb2byt(self,pb):
        self.pcbyt = pb * (1024 ** 5)
        return self.pcbyt

    def pb2kb(self,pb):
        self.pcbyt = pb * (1024 ** 4)
        return self.pcbyt

    def pb2mb(self,pb):
        self.pcbyt = pb * (1024 ** 3)
        return self.pcbyt

    def pb2gb(self,pb):
        self.pcbyt = pb * (1024 ** 2)
        return self.pcbyt

    def pb2tb(self,pb):
        self.pcbyt = pb * 1024
        return self.pcbyt
    
    def pb2eb(self,pb):
        self.pcbyt = pb / 1024
        return self.pcbyt

    def pb2zb(self,pb):
        self.pcbyt = pb / (1024 ** 2)
        return self.pcbyt

    def pb2yb(self,pb):
        self.pcbyt = pb / (1024 ** 3)
        return self.pcbyt

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