"""File for helper functions"""
from typing import Union
from tokenizer import Token, TokenType
from collections import Counter

TokenList = Union[Token, list[Token]]
Literals = [TokenType.NUMBER, TokenType.STRING]


def gettypes(*a):
    return list(map(type, a))


def typecheck(args: list, types: list, *, ordered=True):
    if not ordered:
        return Counter(gettypes(*args)) == Counter(types)
    else:
        return gettypes(*args) == types


def typecheckAny(arg: Union[int, str], types: list):
    types = [typecheck(args=[arg], types=[typ]) for typ in types]
    return any(types)
