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
    """

    if not ordered:
        return Counter(gettypes(*args)) == Counter(types)
    else:
        instance = []
        for ind in range(len(args)):
            instance.append(isinstance(args[ind], types[ind]))
        return instance


def typecheckAny(arg: Union[int, str], types: list):
    types = [typecheck(args=[arg], types=[typ]) for typ in types]
    return any(types)
