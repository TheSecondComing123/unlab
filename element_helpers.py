import itertools


def add(a: int, b: int):
    return a + b


def subtract(a: int, b: int):
    return a - b


def multiply(a: int, b: int):
    return a * b


def divide(a: int, b: int):
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


def interleaveStr(a: str, b: str):
    """Interleave a and b (two strings)"""
    a_list, b_list = list(a), list(b)
    return "".join(interleave(a_list, b_list))


def print_with_newline(a):
    """Format a as a string with newline"""
    if callable(a):
        return str(a())  # For constants (which are stored as lambdas)
    return str(a) + "\n"


def power(a, b):
    """Take the power of a and b"""
    # fmt: off
    return a ** b
    # fmt: on
