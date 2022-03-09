"""File for helper functions"""
from typing import Union
from tokenizer import Token, TokenType
from collections import Counter

TokenList = Union[Token, list[Token]]
Literals = [TokenType.NUMBER, TokenType.STRING]
Rational = (int, float)


def gettypes(*a):
    """
    Convert a list of objects to their types
    """
    return list(map(type, a))


def typecheck(args: list, types: list, *, ordered=True):
    """
    Check if the types of args match types. If ordered is true,
    the check order is strict.

    If the length of types > 1 and the length of args is one,
    check if the only item in args is any of the types in types
    and return it.
    """

    try:
        if not ordered:
            return Counter(gettypes(*args)) == Counter(types)
        else:
            if len(args) == len(types):
                return all(isinstance(a, b) for a, b in zip(args, types))
            elif len(args) == 1 and len(types) > 1:
                for t in types:
                    if isinstance(args[0], t):
                        return t
                return False
    except (TypeError, IndexError):
        raise TypeError(f"Did you mean: [{args}]?") from None


def typecheck_any(arg: Union[int, str], types: list):
    types = [typecheck(args=[arg], types=[typ]) for typ in types]
    return any(types)
