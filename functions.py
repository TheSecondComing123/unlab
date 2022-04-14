from helper import *
from context import Context
from element_helpers import *
from helper import Rational

g = "Hello, World!"
w = "Hello World"
b = "0123456789"
o = "123456789"
a = "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = 10
d = 16
e = 256
f = -1
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
    """Addition/Concatenation"""
    if typecheck(args=[a, b], types=[Rational, Rational]):
        return add(a, b)
    elif typecheck(args=[a, b], types=[str, str]):
        return concat(a, b)
    elif typecheck(args=[a, b], types=[str, Rational]):
        return concat(a, b)
    elif typecheck(args=[a, b], types=[Rational, str]):
        return addascii(a, b)


def Sub(a, b, ctx=ctx):
    """Subtraction"""
    if typecheck(args=[a, b], types=[Rational, Rational]):
        return subtract(a, b)
    elif typecheck(args=[a, b], types=[str, str]):
        return removechars(a, b)


def Mul(a, b, ctx=ctx):
    """Multiplication"""
    if typecheck(args=[a, b], types=[Rational, Rational]):
        return multiply(a, b)
    elif typecheck(args=[a, b], types=[str, str]):
        return joinab(a, b)
    elif typecheck(args=[a, b], types=[str, int]):
        return repeat(a, b)


def TrueDiv(a, b, ctx=ctx):
    """Division"""
    if typecheck(args=[a, b], types=[Rational, Rational]):
        return divide(a, b)


def Print(a, ctx=ctx):
    """Print with newline"""
    ctx.print += print_with_newline(a)
    ctx.printed = True
    return a


def Power(a, b, ctx=None):
    """Exponentiation"""
    if typecheck(args=[a, b], types=[Rational, Rational]):
        return power(a, b)
    elif typecheck(args=[a, b], types=[str, str]):
        return interleave(a, b)


def SumDigits(a, ctx=None):
    if typecheck(args=[a], types=[int]):
        return sumdigits(a)
    elif typecheck(args=[a], types=[str]):
        return sumascii(a)


def GeneralInput(ctx=None):
    return general_input()


def Mod(a, b, ctx=None):
    if typecheck(args=[a, b], types=[int, int]):
        return mod(a, b)


def ExclamationMark(a, ctx=None):
    if typecheck(args=[a], types=[str]):
        return uppercase(a)
    elif typecheck(args=[a], types=[Rational]):
        return add(a, 1)


def InversExclamation(a, ctx=None):
    if typecheck(args=[a], types=[str]):
        return lowercase(a)
    elif typecheck(args=[a], types=[Rational]):
        return subtract(a, 1)


def HollowSquare(a, ctx=None):
    if typecheck(args=[a], types=[str]):
        return swapcase(a)
    elif typecheck(args=[a], types=[Rational]):
        return negate(a)


def Index(a, b, ctx=None):
    return index(safe_cast(a, str), safe_cast(b, int))


def Slice(a, b, c, ctx=None):
    return slice(safe_cast(a, str),
                 safe_cast(b, int),
                 safe_cast(c, int))


def Head(a, b, ctx=None):
    return head(safe_cast(a, str), safe_cast(b, int))


def Tail(a, b, ctx=None):
    return tail(safe_cast(a, str), safe_cast(b, int))
