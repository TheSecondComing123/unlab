from helper import *
from context import Context
from element_helpers import *

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
p6 = 4096
p7 = 1024
p8 = 128


ctx = Context()  # Set ctx to Context() at first (and as a default)
# when nothing is given


def Add(a, b, ctx=ctx):
    """Addition/Concatanation"""
    if typecheck(args=[a, b], types=[int, int]):
        return add(a, b)
    elif typecheck(args=[a, b], types=[str, str]):
        return concat(a, b)


def Sub(a, b, ctx=ctx):
    """Subtract"""
    if typecheck(args=[a, b], types=[int, int]):
        return subtract(a, b)


def Mul(a, b, ctx=ctx):
    """Multiplication"""
    if typecheck(args=[a, b], types=[int, int]):
        return multiply(a, b)
    elif typecheck(args=[a, b], types=[str, str]):
        return joinab(a, b)


def TrueDiv(a, b, ctx=ctx):
    """Division"""
    if typecheck(args=[a, b], types=[int, int]):
        return divide(a, b)


def Print(a, ctx=ctx):
    """Print with newline"""
    ctx.print = print_with_newline(a)
    ctx.printed = True
    return a


def Power(a, b, ctx=None):
    """Exponentiation"""
    if typecheck(args=[a, b], types=[int, int]):
        return power(a, b)
    elif typecheck(args=[a, b], types=[str, str]):
        return interleave(a, b)
