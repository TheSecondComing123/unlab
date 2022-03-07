"""File for helper functions"""
from typing import Union
from tokenizer import Token, TokenType
from collections import Counter

TokenList = Union[Token, list[Token]]
Literals = [TokenType.NUMBER, TokenType.STRING]
Rational = (int, float)


def gettypes(*a):
    return list(map(type, a))


def typecheck(args: list, types: list, *, ordered=True):
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
