"""File for helper functions"""
from typing import Union
from tokenizer import Token, TokenType
from collections import Counter

TokenList = Union[Token, list[Token]]
Literals = [TokenType.NUMBER, TokenType.STRING]


def Types(*a):
    return list(map(type, a))


def IsType(args, types):
    return Counter(Types(*args)) == Counter(types)
