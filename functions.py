from helper import typecheck
import itertools

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


def Add(a1, a2, ctx=None):
    """Add two numbers"""
    if typecheck(args=[a1, a2], types=[str, int]):
        return str(a1) + str(a2)
    else:
        return a1 + a2


def Sub(a1, a2, ctx=None):
    """Subtract two numbers"""
    return a1 - a2


def Mul(a1, a2, ctx=None):
    """Multiplies too numbers"""
    return a1 * a2


def TrueDiv(a1, a2, ctx=None):
    """Divides two numbers"""
    if a2 == 0:
        return float(
            f"{'-' if a1 < 0 else ''}Infinity"
        )  # Although negative numbers are not supported (yet)

    return a1 / a2


def Print(a1, ctx=None):
    """Prints something"""
    ctx.print += str(a1) + "\n"
    ctx.printed = True

    return a1


def Power(a1, a2, ctx=None):
    """Calculates a1 to the power of a2"""
    # fmt: off
    return a1 ** a2
    # fmt: on


def _interleave(a1, a2):
    """Interleave a1 and a2 (two iterables)"""

    a2 = itertools.cycle(a2)
    convert_func = "".join if isinstance(a1, str) else type(a1)
    return convert_func(itertools.chain.from_iterable(zip(a1, a2)))
