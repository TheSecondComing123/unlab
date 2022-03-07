import itertools
from typing import Union, Callable, Iterable
from numbers import Rational


def add(a: Rational, b: Rational):
    return a + b


def subtract(a: Rational, b: Rational):
    return a - b


def multiply(a: Rational, b: Rational):
    return a * b


def divide(a: Rational, b: Rational):
    if b == 0:
        return float(
            f"{'-' if a < 0 else ''}Infinity"
        )  # Although negative numbers are not supported (yet)
    return a / b


def concat(a: str, b: str):
    """Concat two strings"""
    return a + b


def interleave(a: list, b: list):
    """Interleave a and b (two iterables)"""

    b_cycle = itertools.cycle(b)
    convert_func = "".join if isinstance(a, str) else type(a)
    return convert_func(itertools.chain.from_iterable(zip(a, b_cycle)))


def print_with_newline(a: Union[str, Callable]):
    """Format a as a string with newline, a:str"""
    if callable(a):
        return str(a())  # For constants (which are stored as lambdas)
    return str(a) + "\n"


def power(a: Rational, b: Rational):
    """Take the power of a and b, a:int, b:int"""
    # fmt: off
    return a ** b
    # fmt: on


def joinab(a: Iterable, b: str):
    """b.join(a), a:Iterable[Any, Not[Int]], b:str"""
    return b.join(a)
