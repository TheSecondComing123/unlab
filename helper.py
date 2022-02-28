"""File for helper functions"""
from typing import Union
from tokenizer import Token, TokenType
from collections import Counter

TokenList = Union[Token, list[Token]]
Literals = [TokenType.NUMBER, TokenType.STRING]


def gettypes(*a):
    return list(map(type, a))


def typecheck(args, types, *, ordered=False):
    if not ordered:
        return Counter(gettypes(*args)) == Counter(types)
    else:
        return gettypes(*args) == types
