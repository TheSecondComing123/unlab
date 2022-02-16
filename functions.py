g = "Hello, World!"
w = "Hello World"
b = "0123456789"
o = "123456789"
a = "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = 10
d = 16
e = 256
f = 32768
h = 65536
i = 2048
j = 4906
k = 1024
l = 128
n = -1
p0 = 10
p1 = 16
p2 = 256
p3 = 32768
p4 = 65536
p5 = 2048
p6 = 4906
p7 = 1024
p8 = 128


def Add(a1, a2, ctx=None):
    """Add two numbers"""
    return a1 + a2


def Sub(a1, a2, ctx=None):
    """Subtract two numbers"""
    return a1 - a2


def Mul(a1, a2, ctx=None):
    """Multiplies too numbers"""
    return a1 * a2


def TrueDiv(a1, a2, ctx=None):
    """Divides two numbers"""
    return a1 / a2


def Print(a1, ctx=None):
    """Prints something"""
    ctx.print += str(a1) + "\n"
    ctx.printed = True

    return a1
